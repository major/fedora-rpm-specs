Name:           python-opentypesvg
Version:        1.1.5
Release:        %autorelease
Summary:        Tools for making OpenType-SVG fonts

License:        MIT
URL:            https://github.com/adobe-type-tools/opentype-svg
Source:         %{pypi_source opentypesvg}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Tools for making OpenType-SVG fonts

- addsvg adds an SVG table to a font, using SVG files provided. The font's
  format can be either OpenType or TrueType.

- dumpsvg saves the contents of a font's SVG table as individual SVG files. The
  font's format can be either OpenType, TrueType, WOFF, or WOFF2.

- fonts2svg generates a set of SVG glyph files from one or more fonts and hex
  colors for each of them. The fonts' format can be either OpenType, TrueType,
  WOFF, or WOFF2.}


%description %_description

%package -n     python3-opentypesvg
Summary:        %{summary}

%description -n python3-opentypesvg %_description


%prep
%autosetup -p1 -n opentypesvg-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l opentypesvg


%check
%pyproject_check_import
%pytest

%files -n python3-opentypesvg -f %{pyproject_files}
%doc README.md
%{_bindir}/addsvg
%{_bindir}/dumpsvg
%{_bindir}/fonts2svg

%changelog
%autochangelog
