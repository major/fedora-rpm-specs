Name:           shybrid
Version:        0.4.3
Release:        %autorelease
Summary:        GUI for generating hybrid ground-truth spiking data

License:        GPLv3+
URL:            https://github.com/jwouters91/shybrid
Source0:        %{pypi_source shybrid}
Source1:        %{name}.desktop

BuildArch:      noarch 
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib-qt5
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       python3-matplotlib-qt5

%description
SHYBRID is a graphical user interface that allows 
for the easy creation of hybrid ground 
truth extracellular recordings

%prep
%autosetup -n shybrid-%{version}
sed -i 's/PyQt5==5.13/PyQt5>=5.13/' setup.py

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l hybridizer
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{SOURCE1}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.*
%{_bindir}/shybrid
%{_datadir}/applications/%{name}.desktop


%changelog
%autochangelog
