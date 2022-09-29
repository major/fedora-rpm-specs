Name:           go2rpm
Version:        1.8.2
Release:        %autorelease
Summary:        Convert Go packages to RPM

License:        MIT
URL:            https://pagure.io/GoSIG/go2rpm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       askalono-cli
Requires:       compiler(go-compiler)

%description
Convert Go packages to RPM.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{name}

%files  -f %{pyproject_files}
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
