Name:           alot
Version:        0.11
Release:        4%{?dist}
Summary:        Experimental terminal MUA based on notmuch mail

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/pazz/alot
Source0:        %{url}/archive/%{version}/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# needed to generate manpages
BuildRequires:  python3-sphinx
BuildRequires:  make

%description
alot makes use of existing solutions where possible: It does not fetch, send or
edit mails; it lets notmuch handle your mailindex and uses a toolkit to render
its display. You are responsible for automatic initial tagging.

%prep
%autosetup -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%make_build man PYTHONPATH=${PYTHONPATH}:$RPM_BUILD_DIR/alot-%{version} SPHINX_BUILD=sphinx-build-3 PYTHON=python3 -C docs

%install
%pyproject_install
%pyproject_save_files -l alot
install -Dpm0644 docs/build/man/alot.1* -t %{buildroot}%{_mandir}/man1/
install -Dpm0644 alot/defaults/* -t %{buildroot}/%{python3_sitelib}/alot/defaults/

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license COPYING
%doc NEWS README.md
%{_bindir}/alot
%{_mandir}/man1/alot.1*
%{python3_sitelib}/alot/defaults

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Miro Hrončok <mhroncok@redhat.com> - 0.11-3
- Run import check during the build

* Thu Nov 14 2024 Tomas Tomecek <ttomecek@redhat.com> - 0.11-2
- Install defaults

* Mon Aug 26 2024 Packit <hello@packit.dev> - 0.11-1
- New upstream release 0.11

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10-4
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 14 2023 Packit <hello@packit.dev> - 0.10-1
- New upstream release 0.10

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.8.1-16
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.1-13
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-10
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.8.1-1
- Update to 0.8.1
- s/python 2/python 3/
- Clean spec a bit.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.7-1
- Update to 0.7

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-1
- Update to 0.6
- Cleanup spec

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.4-1
- update to 0.4

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.6-5
- Rebuild for gpgme 1.18

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug 12 2014 Tomas Tomecek <ttomecek@redhat.com> - 0.3.6-1
- initial package

