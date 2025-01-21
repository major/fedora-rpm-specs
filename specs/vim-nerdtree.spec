Name:           vim-nerdtree
Version:        6.10.16
Release:        6%{?dist}
Summary:        A tree explorer plugin for the editor Vim

License:        WTFPL
URL:            https://github.com/preservim/nerdtree
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Added metainfo per 
# https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/#_metainfo_xml_file_creation
Source1:        vim-nerdtree.metainfo.xml

Requires:       vim-common

# TODO: These are needed by %%transfiletrigger provided by vim-commons,
# not sure how to get rid of these ATM :/
Requires(post): vim
Requires(postun): vim

# Needed for AppData check.
BuildRequires:  libappstream-glib

# Defines %%vimfiles_root
BuildRequires:  vim-filesystem
BuildArch:      noarch

%description
The NERD tree allows you to explore your filesystem and to open files and
directories. It presents the filesystem to you in the form of a tree which
you manipulate with the keyboard and/or mouse. It also allows you
to perform simple filesystem operations.


%prep
%setup -q -n nerdtree-%{version}


%build
# Nothing to build. We are just copying files to the filesystem


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {autoload,doc,lib,nerdtree_plugin,plugin,syntax} %{buildroot}%{vimfiles_root}

# Install AppData.
mkdir -p %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE1} %{buildroot}%{_metainfodir}


%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc CHANGELOG.md
%license LICENCE
%doc README.markdown
%doc %{vimfiles_root}/doc/NERDTree.txt
%{vimfiles_root}/autoload/nerdtree
%{vimfiles_root}/autoload/nerdtree.vim
%dir %{vimfiles_root}/lib
%{vimfiles_root}/lib/nerdtree
%{vimfiles_root}/nerdtree_plugin/
%{vimfiles_root}/plugin/NERD_tree.vim
%{vimfiles_root}/syntax/nerdtree.vim
%{_metainfodir}/vim-nerdtree.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Robby Callicotte <rcallicotte@fedoraproject.org> - 6.10.16-1
- Rebased to new version
- Resolves bz #2105772

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Vít Ondruch <vondruch@redhat.com> - 5.0.0-1
- Update to NERDTree 5.0.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Till Maas <opensource@till.name> - 4.2.0-8
- Update summary (#891122)

* Fri Aug 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-7
- Fixed the Deactivating folds patch to apply cleanly.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-5
- Add the missing Group tag.

* Mon Apr 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-4
- Applied upstream patch as requested in RHBZ #812360.
- Add post and postun Requires: vim (to generate helptags properly).

* Thu Jan 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-3
- Added %%preun and %%postun to properly re-generate vim doc tags.

* Wed Jan 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-2
- Fixed issues from the review request (RHBZ #784021).

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 4.2.0-1
- Initial package.
