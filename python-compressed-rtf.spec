%global pypi_name compressed-rtf
%global forgeurl https://github.com/delimitry/compressed_rtf
# PyPI release is missing LICENSE file, but upstream has no tags nor
# releases on GitHub. So we pull from the release commit.
%global commit ad93a504ca6a09aff9561eac586ff6d91861d147

Name:           python-%{pypi_name}
Version:        1.0.6
%forgemeta
Release:        %{autorelease}
Summary:        Compressed Rich Text Format (RTF) (de-)compression
License:        MIT
URL:            %forgeurl
Source:         %forgesource
# Fix shebang
Patch:          %{forgeurl}/pull/11.patch
# Include LICENSE
Patch:          %{forgeurl}/pull/12.patch
# Include `tests/` in sdist
Patch:          %{forgeurl}/pull/13.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Compressed RTF also known as "LZFu" compression format.

Based on Rich Text Format (RTF) Compression Algorithm:

https://msdn.microsoft.com/en-us/library/cc463890(v=exchg.80).aspx}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files compressed_rtf


%check
%pytest -v tests/tests.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
