%global srcname landslide

Name:		python-%{srcname}
Version:	2.0.0
Release:	%autorelease
Summary:	Lightweight markup language-based html5 slideshow generator

License:	Apache-2.0
URL:		https://pypi.python.org/pypi/%{srcname}
Source0:	%{pypi_source}
Patch0:         %{srcname}-2.0.0-make_unversioned.diff

BuildArch:	noarch

%global _description %{expand:
Takes your Markdown, ReST, or Textile file(s) and generates 
fancy HTML5 slideshows.}

%description %_description

%package -n python3-%{srcname}
Summary:	%{summary}

BuildRequires:	python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove shebang, main.py is not invoked directly
touch -r landslide/main.py landslide/main.py.tstamp
sed -i '1d' landslide/main.py
touch -r landslide/main.py.tstamp landslide/main.py
rm landslide/main.py.tstamp

# Remove bundled egg-info
rm -rf landslide.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{srcname}


%check
%pytest -v tests.py


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md examples
%license LICENSE
%{_bindir}/landslide


%changelog
%autochangelog
