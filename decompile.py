import subprocess
from pathlib import Path

import click
from tqdm import tqdm

from tools.StarResonanceMetadata.dump_global_metadata import extract_metadata

IL2CPP_DUMPER_PROJECT = Path("./tools/Il2CppDumper/Il2CppDumper")
STAR_RESONANCE_TOOL_PROJECT = Path("./tools/StarResonanceTool/StarResonanceTool")


@click.command()
@click.argument("dump-file", type=click.Path(dir_okay=False, path_type=Path))
@click.argument("star-data-path", type=click.Path(file_okay=False, path_type=Path))
@click.argument("output", type=click.Path(file_okay=False, path_type=Path))
def main(dump_file: Path, star_data_path: Path, output: Path) -> None:
    game_assembly_file = star_data_path / ".." / "GameAssembly.dll"
    meta_pkg_file = star_data_path / "StreamingAssets" / "container" / "meta.pkg"

    global_metadata_output = output / "global-metadata.dat"
    dummy_dll_output = IL2CPP_DUMPER_PROJECT / "bin" / "Debug" / "net6.0" / "DummyDll"
    star_dump_output = output / "Output"

    with tqdm(total=3) as pbar:
        pbar.set_description("Extracting global-metadata.dat")
        extract_metadata(dump_file, global_metadata_output)
        pbar.update(1)

        pbar.set_description("Dumping game into C#")
        subprocess.run(["dotnet", "run", "--project", IL2CPP_DUMPER_PROJECT,
                        "--framework", "net6.0",
                        game_assembly_file, global_metadata_output, dummy_dll_output],
                       input=b"\r\n")
        pbar.update(1)

        pbar.set_description("Generating protobufs and tables")
        subprocess.run(["dotnet", "run", "--project", STAR_RESONANCE_TOOL_PROJECT.resolve(),
                        "--all",
                        "--pkg", meta_pkg_file.resolve(),
                        "--dll", dummy_dll_output.resolve(),
                        "--output", star_dump_output.resolve()],
                       cwd=output)
        pbar.update(1)

        pbar.set_description("Done")


if __name__ == '__main__':
    main()
