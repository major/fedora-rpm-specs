#used for pre-releases:
%global vimfiles_root %{_datadir}/vim/vimfiles
%global _python_bytecompile_extra 0

Name:          vim-jedi
Version:       0.11.2
Release:       6%{?dist}
Summary:       The Jedi vim plugin

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:       LGPL-3.0-only
URL:           https://github.com/davidhalter/jedi-vim
Source0:       https://github.com/davidhalter/jedi-vim/archive/%{version}/jedi-vim-%{version}.tar.gz
Source1:       %{name}.metainfo.xml

#Patch0:        jedi-vim-0.9.0-fix-debug.patch

Requires:      python3-jedi
Requires:      vim-common
BuildRequires: python3-devel
BuildRequires: python3-libs

BuildArch:     noarch

%description
vim-jedi is a VIM binding to the awesome auto completion library Jedi.

%prep
%autosetup -p1 -n jedi-vim-%{version}

cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,after,autoload,ftplugin,plugin} %{buildroot}%{vimfiles_root}
mkdir -p %{buildroot}/%{_datadir}/appdata
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/

mkdir -p %buildroot/%python3_sitelib
install -m 644 pythonx/*.py %buildroot/%python3_sitelib


%files
%doc README.rst AUTHORS.txt LICENSE.txt
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/after/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/plugin/*
%{_datadir}/appdata/%{name}.metainfo.xml
%{python3_sitelib}/jedi_vim.py*
%{python3_sitelib}/jedi_vim_debug.py*
%{python3_sitelib}/__pycache__/jedi_vim*



%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.11.2-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.11.2-3
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 Martin Jackson <mhjacks@swbell.net> - 0.11.2-1
- Update to 0.11.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.11.1-2
- Rebuilt for Python 3.12

* Thu Jan 12 2023 Martin Jackson <mhjacks@swbell.net> - 0.11.1-1
- Update to 0.11.1 for bz#2145031

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 24 2021 Martin Jackson <mhjacks@fedoraproject.org> - 0.11.0-2
- Upgrade to 0.11.0.  Fixes rhbz#1981998 and rhbz#1742022. 

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Petr Hracek <phracek@redhat.com> - 0.9.0-2
- Get rid off python2 (rhbz#1686429)

* Mon Feb 25 2019 Pavel Raiskup <praiskup@redhat.com> - 0.9.0-1
- new upstream version (rhbz#1559214)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Petr Hracek <phracek@redhat.com> - 0.8.0-1
- Update to the latest upstream version (#1301314)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Petr Hracek <phracek@redhat.com> - 0.7.0-7
- Standard installation of vim-jedi is broken (#1190187)

* Thu Feb 26 2015 Petr Hracek <phracek@redhat.com> - 0.7.0-6
- Add Addon metadata for GNOME Software (#1128812)
- Previous fix was totally wrong

* Wed Feb 25 2015 Petr Hracek <phracek@redhat.com> - 0.7.0-5
- Add Addon metadta for GNOME Software (#1128812)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 18 2014 Petr Hracek <phracek@redhat.com> - 0.7.0-3
- some files are missing in RPM package (jedi_vim.py)

* Fri Jan 17 2014 Petr Hracek <phracek@redhat.com> - 0.7.0-2
- some files are missing in RPM package

* Wed Jan 15 2014 Petr Hracek <phracek@redhat.com> - 0.7.0-1
- Update to vim-jedi-0.7.0 (#1047228)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Petr Hracek <phracek@redhat.com> - 0.5.0-5
- Correcting BuildRoot macro

* Tue Apr 30 2013 Petr Hracek <phracek@redhat.com> - 0.5.0-4
- Correct license

* Thu Apr 25 2013 Petr Hracek <phracek@redhat.com> - 0.5.0-3
- New source file introduced instead of master
- Clean section and removing buildroot is not needed

* Thu Apr 25 2013 Petr Hracek <phracek@redhat.com> - 0.5.0-2
- Files are stored in vimfiles directory
- added post and postun sections

* Fri Apr 19 2013 Petr Hracek <phracek@redhat.com> - 0.5.0-1
- Initial version
