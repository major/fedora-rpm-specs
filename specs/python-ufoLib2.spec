Name:           python-ufoLib2
Version:        0.18.1
Release:        %autorelease
Summary:        A library to deal with UFO font sources

License:        Apache-2.0
URL:            https://github.com/fonttools/ufoLib2
Source:         %{pypi_source ufolib2}

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras lxml,converters,json,msgpack
BuildOption(install): --assert-license ufoLib2

BuildArch:      noarch

# Required for running tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
ufoLib2 is meant to be a thin representation of the Unified Font Object (UFO)
version 3 data model, intended for programmatic manipulation and fast batch
processing of UFOs.}

%description %_description

%package -n python3-ufoLib2
Summary:        %{summary}

%description -n python3-ufoLib2 %_description

%pyproject_extras_subpkg -n python3-ufoLib2 lxml converters json msgpack

%check -a
%pytest --verbose

%files -n python3-ufoLib2 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
