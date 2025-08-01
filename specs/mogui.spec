%global srcname modules-gui
Name:           mogui
Version:        0.2.2
Release:        8%{?dist}
Summary:        Graphical User Interface for Environment Modules

# icon files are licensed under CC-BY-SA-3.0 terms
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://github.com/cea-hpc/mogui
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       environment-modules

%description
MoGui is a Graphical User Interface (GUI) for Environment Modules. It helps
users selecting modules to load and save module collections.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

install -d %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 mogui/icons/mogui-light/symbolic/apps/environment-modules.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

install -d %{buildroot}%{_datadir}/applications
install -p -m 0644 share/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -d %{buildroot}%{_metainfodir}
install -p -m 0644 share/%{name}.metainfo.xml %{buildroot}%{_metainfodir}/

install -d %{buildroot}%{_sysconfdir}/profile.d
install -d %{buildroot}%{_datadir}/fish/vendor_conf.d
install -p -m 0644 share/setup-env.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -p -m 0644 share/setup-env.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -p -m 0644 share/setup-env.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/%{name}.fish

# "mogui" bin is not needed, as mogui shell function is defined at shell session start
# and desktop file relies on the "mogui-cmd" bin
rm %{buildroot}%{_bindir}/%{name}

%check
%pyproject_check_import
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f %{pyproject_files}
%doc ChangeLog README.md TODO.md
%{_bindir}/%{name}-cmd
%{_bindir}/%{name}-setup-env
%{_sysconfdir}/profile.d/%{name}.csh
%{_sysconfdir}/profile.d/%{name}.sh
%{_datadir}/fish/vendor_conf.d/%{name}.fish
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.2.2-7
- Rebuilt for Python 3.14

* Sat Feb 15 2025 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2.2-6
- Remove pyproject_buildrequires "-t" option as no Tox config is present

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.13

* Sat May 25 2024 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2.2-2
- Fix duplicated license files

* Sun Mar 31 2024 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2.2-1
- Update to 0.2.2
- Test desktop file
- Add AppData file and test it
- Remove environment-modules-gui provides
- Clarify license used for icon files (CC-BY-SA-3.0)

* Fri Mar 29 2024 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2.1-2
- Fix python-leftover-require issue

* Thu Mar 28 2024 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2.1-1
- Update to 0.2.1
- Clarify package summary
- Add ChangeLog file to documentation
- Add mogui desktop file
- Remove "mogui" bin (as "mogui" shell function is defined in environment
  and desktop file relies on "mogui-cmd")
- Use "global" directive instead of "define"

* Wed Mar 27 2024 Xavier Delaruelle <xavier.delaruelle@cea.fr> - 0.2-1
- Initial package
