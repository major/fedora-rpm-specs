%global githubuser OpenTTD
#%%global gitver 660722b680fd6a6c5b421d8eabbf36fcc82635ba
#%%global gitshort %(r=%{gitver}; echo ${r:0:7})

%if 0%{?gitver:1}
  %global srcurl   https://github.com/%{githubuser}/%{name}/archive/%{gitver}.tar.gz#/%{name}-%{gitver}.tar.gz
  %global setuppath %{name}-%{gitver}
%else
  %global srcurl   https://github.com/%{githubuser}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
  %global setuppath %{name}-%{version}
%endif


Name:           nml
Version:        0.7.2
Release:        %autorelease
Summary:        NewGRF Meta Language compiler

License:        GPLv2+
URL:            https://github.com/OpenTTD/nml
Source0:        %{srcurl}

BuildRequires:  gcc
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.


%prep
%autosetup -n %{setuppath}

%build
# fixup version info
echo 'version = "%{version}"' > nml/__version__.py
rm nml/version_update.py

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files nml nml_lz77

gzip docs/nmlc.1
install -Dpm 644 docs/nmlc.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/nmlc.1.gz
rm docs/nmlc.1.gz

 
%files -f %{pyproject_files}
%doc docs/changelog.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1.gz


%changelog
%autochangelog
