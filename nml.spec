Version:        0.7.5

%global forgeurl https://github.com/OpenTTD/nml
%global tag      %{version}
%forgemeta

Name:           nml
Release:        %autorelease
Summary:        NewGRF Meta Language compiler

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  gcc
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.


%prep
%forgeautosetup


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
