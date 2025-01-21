%global vimfiles_root %{_datadir}/vim/vimfiles
%global appdata_dir %{_datadir}/appdata

# do not build debugsource and debuginfo subpackages
%global debug_package %{nil}

Name:           vim-go
Version:        1.28
Release:        7%{?dist}
Summary:        Go development plugin for Vim

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD 
URL:            https://github.com/fatih/vim-go
Source0:        https://github.com/fatih/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

# cannot build as noarch until golang is available on all arches
#BuildArch:      noarch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?golang_arches}%{!?golang_arches:%{ix86} x86_64 %{arm}}

Requires:       vim-common
Requires(post): vim
Requires(postun): vim

Requires:       golang

%description
Go (golang) support for Vim. It comes with predefined sensible settings
(like auto gofmt on save), has auto-complete, snippet support, improved syntax
highlighting, go tool-chain commands, etc...
If needed vim-go installs all necessary binaries for providing seamless Vim
integration with current commands. It's highly customizable and each individual
feature can be disabled/enabled easily.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {autoload,compiler,doc,ftdetect,ftplugin,gosnippets,indent,plugin,rplugin,syntax,templates} \
    %{buildroot}%{vimfiles_root}
# remove version control files
find %{buildroot}%{vimfiles_root} -name .gitignore -o -name .gitkeep -delete

mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}


# up until version 1.22, %%{vimfiles_root}/autoload/go/test-fixtures/fmt/src/imports was a symlink,
# but it changed to a directory in later versions - remove it to avoid conflict
%pretrans -p <lua>
path = rpm.expand('%{vimfiles_root}') .. '/autoload/go/test-fixtures/fmt/src/imports'
st = posix.stat(path)
if st and st.type == 'link' then
    os.remove(path)
end


%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :


%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :


%files
%license LICENSE
%doc README.md
%{vimfiles_root}/autoload/*
%{vimfiles_root}/compiler/*
%{vimfiles_root}/doc/*
%{vimfiles_root}/ftdetect/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/gosnippets/*
%{vimfiles_root}/indent/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/rplugin/*
%{vimfiles_root}/syntax/*
%{vimfiles_root}/templates/*
%{appdata_dir}/%{name}.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Nikola Forró <nforro@redhat.com> - 1.28-1
- Update to 1.28
  Resolves: #2154617

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 24 2022 Nikola Forró <nforro@redhat.com> - 1.26-1
- Update to 1.26
  Resolves: #2075411

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 19 2021 Nikola Forró <nforro@redhat.com> - 1.25-1
- Update to 1.25
  Resolves: #1950879

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Nikola Forró <nforro@redhat.com> - 1.24-1
- Update to 1.24
  Resolves: #1876683

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Nikola Forró <nforro@redhat.com> - 1.23-2
- Fix symlink -> directory conflict

* Tue May 19 2020 Nikola Forró <nforro@redhat.com> - 1.23-1
- Update to 1.23
  Resolves: #1837081

* Fri Jan 31 2020 Nikola Forró <nforro@redhat.com> - 1.22-1
- Update to 1.22
  Resolves: #1792556

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Nikola Forró <nforro@redhat.com> - 1.21-1
- Update to 1.21
  Resolves: #1751453

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Nikola Forró <nforro@redhat.com> - 1.20-2
- Install missing directories
  Resolves: #1704897

* Wed Apr 24 2019 Nikola Forró <nforro@redhat.com> - 1.20-1
- Update to 1.20
  Resolves: #1702385

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Nikola Forró <nforro@redhat.com> - 1.19-1
- Update to 1.19

* Thu Jul 19 2018 Nikola Forró <nforro@redhat.com> - 1.18-1
- Update to 1.18
  Resolves #1602979

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Nikola Forró <nforro@redhat.com> - 1.17-1
- Update to 1.17
  Resolves #1561259

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Nikola Forró <nforro@redhat.com> - 1.16-1
- Update to 1.16
  Resolves #1529822

* Fri Oct 20 2017 Nikola Forró <nforro@redhat.com> - 1.15-1
- Update to 1.15
  Resolves #1504459

* Tue Sep 26 2017 Nikola Forró <nforro@redhat.com> - 1.14-2
- Make package architecture specific on Fedora

* Fri Aug 25 2017 Nikola Forró <nforro@redhat.com> - 1.14-1
- Update to 1.14
  Resolves #1485386

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Nikola Forró <nforro@redhat.com> - 1.13-1
- Update to 1.13
  Resolves #1459151

* Fri Mar 31 2017 Nikola Forró <nforro@redhat.com> - 1.12-1
- Update to 1.12
  Resolves #1437703

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Nikola Forró <nforro@redhat.com> - 1.11-1
- Update to 1.11
  Resolves #1411559

* Tue Nov 29 2016 Nikola Forró <nforro@redhat.com> - 1.10-1
- Update to 1.10
  Resolves #1398310

* Thu Sep 15 2016 Nikola Forró <nforro@redhat.com> - 1.9-1
- Update to 1.9
  Resolves #1376315

* Wed Aug 10 2016 jchaloup <jchaloup@redhat.com> - 1.8-3
- No ppc for epel7
  related: #1361932

* Sat Aug 06 2016 jchaloup <jchaloup@redhat.com> - 1.8-2
- build section is empty => no Golang needed
  related: #1361932

* Mon Aug 01 2016 Nikola Forró <nforro@redhat.com> - 1.8-1
- Update to 1.8
  Resolves #1361932

* Wed Jun 08 2016 Nikola Forró <nforro@redhat.com> - 1.7.1-1
- Update to 1.7.1
  Resolves #1343269

* Tue Apr 26 2016 Nikola Forró <nforro@redhat.com> - 1.6-1
- Update to 1.6
  Resolves #1330382

* Thu Mar 17 2016 Nikola Forró <nforro@redhat.com> - 1.5-1
- Update to 1.5
  Resolves #1318468

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Nikola Forró <nforro@redhat.com> - 1.4-2
- Fix mode of non-executable files

* Wed Jan 20 2016 Nikola Forró <nforro@redhat.com> - 1.4-1
- Updated to 1.4
  Resolves #1300128

* Mon Nov 23 2015 Nikola Forró <nforro@redhat.com> - 1.3-1
- Updated to 1.3
  Resolves #1284252

* Fri Oct 02 2015 Nikola Forró <nforro@redhat.com> - 1.2-1
- Updated to 1.2
  Resolves #1268172

* Wed Jul 29 2015 Nikola Forró <nforro@redhat.com> - 1.1-1
- Updated to 1.1
- Added license file
  Resolves #1247667

* Mon Jul 27 2015 Nikola Forró <nforro@redhat.com> - 1.0.5-5
- Added Gnome Software plug-in AppData
- Added missing ExclusiveArch and BuildRequires

* Fri Jul 24 2015 Nikola Forró <nforro@redhat.com> - 1.0.5-4
- Handled exit codes of commands in scriptlets
- Unmarked doc directory previously marked as %%doc

* Thu Jul 23 2015 Nikola Forró <nforro@redhat.com> - 1.0.5-3
- Require golang
- Added command to %%postun to clear vim tags

* Thu Jul 23 2015 Nikola Forró <nforro@redhat.com> - 1.0.5-2
- Removed unneeded rm command in %%postun section

* Tue Jul 21 2015 Nikola Forró <nforro@redhat.com> - 1.0.5-1
- Initial package
