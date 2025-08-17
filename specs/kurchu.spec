%global koji_minver 1.35

Name:           kurchu
Version:        0.4.3
Release:        4%{?dist}
Summary:        Assembles Fedora/CentOS resources to create artifact collections

License:        GPL-2.0-or-later
URL:            https://gitlab.com/VelocityLimitless/Projects/%{name}
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  scdoc
Requires:       git-core
Requires:       koji >= %{koji_minver}
Requires:       python3-koji-cli-plugins >= %{koji_minver}
Requires:       lftp
Requires:       s3cmd
Requires:       tree

%description
%{summary}.


%prep
%autosetup -S git_am


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -L %{name}

mkdir -p %{buildroot}%{_mandir}/man5
scdoc < docs/%{name}.toml.5.scd > %{buildroot}%{_mandir}/man5/%{name}.toml.5

%check
%pytest


%files -f %{pyproject_files}
%license COPYING
%doc README.md examples
%{_bindir}/%{name}
%{_mandir}/man5/%{name}.toml.5*


%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.4.3-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.14

* Tue May 06 2025 Neal Gompa <ngompa@velocitylimitless.com> - 0.4.3-1
- Initial package
