Star Resonance Dumper Utility
=============================

Script to generate BPSR dump like https://github.com/PotRooms/StarResonanceData

## Requirements

- [uv](https://docs.astral.sh/uv/)
- [.NET SDK 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

## Usage

```shell
git submodule update --init --recursive
```

```shell
uv run decompile.py <star.dmp> <star_data_dir> <out_dir>
```

## Credits

- [rushkii/StarResonaceMetadata](https://github.com/rushkii/StarResonanceMetadata) - Extracting the global-metadata.dat from game memory dump.
- [Perfare/Il2CppDumper](https://github.com/Perfare/Il2CppDumper) - Dumping Unity DLLs.
- [PotRooms/StarResonanceTool](https://github.com/PotRooms/StarResonanceTool) - Parsing and dumping BPSR protobufs and tables.

## Disclaimer

This project is in no form related, associated, or endorsed by the developer and publisher of Blue Protocol: Star Resonance.
The project is created for educational purposes only.
