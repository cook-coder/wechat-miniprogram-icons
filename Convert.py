from Export import Export
from SvgReader import SvgReader

# Execute converting process.
if __name__ == "__main__":
    svg_reader = SvgReader()
    data = svg_reader.get_svg_data()
    for project_name in data:
        exportor = Export(project_name)
        exportor.export(data[project_name])
