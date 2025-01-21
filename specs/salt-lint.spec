Name:           salt-lint
Version:        0.9.2
Release:        7%{?dist}
Summary:        Salt State file (SLS) lint tool

License:        MIT
URL:            https://github.com/warpnet/salt-lint
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# This is a downstream only patch persuant to
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch0:         00-remove-linter-deps.patch

BuildRequires:  python3-devel
BuildArch:      noarch

%description
salt-lint checks Salt State files (SLS) for best practices and behavior that
could potentially be improved.


%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files saltlint
install -Dpm 0644 docs/man/salt-lint.1 %{buildroot}%{_mandir}/man1/salt-lint.1



%check
%tox


%files -f %{pyproject_files}
%license LICENSE*
%doc README.*
%{_bindir}/%{name}
%{_mandir}/man1/salt-lint.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.2-5
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.9.2-2
- Rebuilt for Python 3.12

* Sun Feb 26 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.9.2-1
- Rebased to new version
  Resolves rhbz#2168759

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 0.9.1-1
- Rebased to new version
  Resolves rhbz#2160859

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Robby Callicotte <rcallicotte@mailbox.org> - 0.8.0-1
- Version bump

* Mon Nov 01 2021 Robby Callicotte <rcallicotte@mailbox.org> - 0.7.0-1
- Version bump

* Sat Oct  9 2021 Robby Callicotte <rcallicotte@mailbox.org> - 0.6.1-1
- Initial build
