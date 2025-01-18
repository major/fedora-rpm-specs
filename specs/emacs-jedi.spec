%global pkg jedi

%global commit e942a0e410cbb2a214c9cb30aaf0e47eb0895b78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210503

Name:           emacs-%{pkg}
Version:        0.3.0
Release:        0.13.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Python auto-completion for Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://tkf.github.io/%{name}/
Source0:        https://github.com/tkf/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{pkg}-init.el
# Remove useless dependency on argparse module (in Python standard library)
Patch0:         %{name}-0.3.0-python_requires.patch
# Invoke system jediepcserver
Patch1:         %{name}-0.2.8-jediepcserver.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-epc
BuildRequires:  emacs-python-environment
BuildRequires:  python3-devel
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-auto-complete
Requires:       emacs-epc
Requires:       emacs-python-environment
Requires:       %{py3_dist jediepcserver}
BuildArch:      noarch

%description
Jedi.el is a Python auto-completion package for Emacs. It aims at helping your
Python coding in a non-destructive way. It also helps you to find information
about Python objects, such as docstring, function arguments and code location.


%package -n python3-jediepcserver
Summary:        Jedi EPC server
Provides:       jediepcserver = %{version}-%{release}

%description -n python3-jediepcserver
%{summary}.


%prep
%autosetup -n %{name}-%{commit}

# Remove shebang
sed -i.orig -e 1d jediepcserver.py && \
touch -r jediepcserver.py.orig jediepcserver.py && \
rm jediepcserver.py.orig


%generate_buildrequires
%pyproject_buildrequires -t


%build
%{_emacs_bytecompile} %{pkg}-core.el %{pkg}.el

%pyproject_wheel


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}-core.el* setup.py -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
ln -s %{python3_sitelib}/jediepcserver.py $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/jediepcserver.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%pyproject_install
%pyproject_save_files jediepcserver


%check
export PYTEST_ADDOPTS="--deselect=test_jediepcserver.py::test_epc_server_runs_fine_in_virtualenv"
%tox


%files
%doc CONTRIBUTING.md README.rst
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%files -n python3-jediepcserver -f %{pyproject_files}
%{_bindir}/jediepcserver


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.13.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-0.12.20210503gite942a0e
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.11.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-0.10.20210503gite942a0e
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.9.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.8.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.7.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.3.0-0.6.20210503gite942a0e
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.5.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.4.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-0.3.20210503gite942a0e
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.2.20210503gite942a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.3.0-0.1.20210503gite942a0e
- Update to latest snapshot (for jedi >= 0.18 support)

* Sat Sep 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-5
- Add Python tests
- Update autostart file

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.8-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-1
- Initial RPM release
