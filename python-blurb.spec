Name:           python-blurb
Version:        1.1.0
Release:        7%{?dist}
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries

License:        BSD
URL:            https://github.com/python/core-workflow/tree/master/blurb
Source:         %pypi_source blurb %{version}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%package -n     python3-blurb
Summary:        %{summary}
Provides:       blurb = %{version}-%{release}

# Calls git in subprocess
Requires:       /usr/bin/git

%description -n python3-blurb
Blurb is a tool designed to rid CPython core development of the scourge of
Misc/NEWS conflicts.

%prep
%autosetup -n blurb-%{version}

# script in site-packages
sed -i '1d' blurb.py
chmod -x blurb.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files blurb

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/blurb --help

%files -n python3-blurb -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/blurb

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Petr Viktorin <pviktori@redhat.com> - 1.1.0-1
- Version 1.1.0
  Support GitHub Issues in addition to b.p.o (bugs.python.org).

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-6
- In %%check, test blurb --help

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.8-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.8-2
- Backport patch to replace flit.ini with pyproject.toml needed by flit 3.0.0
- Convert spec to use pyproject-rpm-macros

* Thu Sep 24 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.0.8-1
- Update to 1.0.8
- Only require /usr/bin/git, not full git

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-1
- Update to upstream 1.0.7 (#1598195)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Petr Viktorin <pviktori@redhat.com> - 1.0.5-1
- Update to upstream 1.0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.post1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-1.post1
- rebuilt
