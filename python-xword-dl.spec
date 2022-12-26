%global pypi_name xword_dl

Name:           python-xword-dl
Version:        2022.12.14
Release:        %autorelease
Summary:        Download tool for online crossword puzzles

License:        MIT
URL:            https://github.com/thisisparker/xword-dl
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
xword-dl is a command-line tool to download .puz files for online crossword
puzzles from supported outlets or arbitrary URLs with embedded crossword
solvers. For a supported outlet, you can easily download the latest puzzle, or
specify one from the archives.}

%description %_description

%package -n     python3-xword-dl
Summary:        %{summary}

%description -n python3-xword-dl %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Relax dependencies version pinning
sed -i requirements.txt -e '/bs4/d' -e 's/==.*$//g'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Remove leftovers installed in the wrong place
rm %{buildroot}%{_prefix}/{LICENSE,requirements.txt}

%check
%pyproject_check_import

%files -n python3-xword-dl -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/xword-dl

%changelog
%autochangelog
