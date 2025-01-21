%global gem_name narray

Name:           rubygem-%{gem_name}
Version:        0.6.1.2
Release:        1%{?dist}
Summary:        N-dimensional Numerical Array class for Ruby

# Automatically converted from old format: BSD and Ruby - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Ruby
URL:            http://%{gem_name}.rubyforge.org
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Patch0000:      https://github.com/masa16/narray/compare/0.6.1.2...master.patch#/%{name}-%{version}-last-commit.patch

BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
NArray is a Numerical N-dimensional Array class.  Supported element types are
1/2/4-byte Integer, single/double-precision, Real/Complex and Ruby Object.
This extension library incorporates fast calculation and easy manipulation of
large numerical arrays into the Ruby language.  NArray has features similar to
NumPy, but NArray has vector and matrix sub-classes.


%package devel
Summary:        Development files and developer's docs for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}

%description devel
This package contains the development files and the developer's documentation
for %{name}.


%prep
%autosetup -p 1 -n %{gem_name}-%{version}


%build
export CONFIGURE_ARGS="--with-cflags='-std=c99 %{build_cflags}'"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
# Copy to buildroot.
cp -a ./%{_prefix} %{buildroot}

# Clean-up.
pushd %{buildroot}
find .%{gem_instdir} -depth -type f -name '*.so' -print0 | xargs -0 rm -rf
find . -depth -type f -name '.*' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.log' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.o' -print0 | xargs -0 rm -rf
find . -depth -type f -name '*.out' -print0 | xargs -0 rm -rf
find . -depth -size 0 -type f -print0 | xargs -0 rm -rf
rm -rf .%{gem_cache} .%{gem_instdir}/src .%{gem_instdir}/%{gem_name}.gemspec
touch %{buildroot}%{gem_extdir_mri}/gem.build_complete
popd


%files
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/README.*
%dir %{gem_instdir}
%exclude %{gem_instdir}/MANIFEST
%exclude %{gem_instdir}/SPEC.*
%exclude %{gem_extdir_mri}/*.h
%{gem_extdir_mri}
%{gem_spec}


%files devel
%doc %{gem_docdir}
%doc %{gem_instdir}/MANIFEST
%doc %{gem_instdir}/SPEC.*
%{gem_extdir_mri}/*.h


%changelog
* Sun Jan 19 2025 Björn Esser <besser82@fedoraproject.org> - 0.6.1.2-1
- New upstream release
- Add patch with last upstream commits
- Set GCC in C99 mode explicitly
- Build devel package archful
- Drop explicit Requires and Provides

* Sun Jan 19 2025 Björn Esser <besser82@fedoraproject.org> - 0.6.1.1-35
- Remove old cruft from spec file
- Convert tabs to spaces

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1.1-33
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1.1-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.6.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1.1-26
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1.1-24
- F-36: rebuild against ruby31
- Execute %%gem_install on %%build on fedora branch to fix FTBFS with package_notes

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 0.6.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1.1-17
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.6.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 0.6.1.1-13
- Add BuildRequires: gcc, fixes FTBFS (#1606220)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.6.1.1-10
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1.1-9
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.6.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.6.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Björn Esser <bjoern.esser@gmail.com> - 0.6.1.1-1
- new upstream release (#1178432)

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.6.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.9-1
- new upstream release (#1103230)

* Mon May 26 2014 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-14
- preserve `%%{gem_extdir_mri}/gem.build_complete` on Fedora >= 21
- no need to modify gemspec

* Sat May 17 2014 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-13
- fix gemspec on Fedora >= 21
- remove `%%{gem_extdir_mri}/gem_make.out` again

* Sat May 17 2014 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-12
- one must NOT delete `%%{gem_extdir_mri}/gem_make.out`

* Thu May 01 2014 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-11
- rebuilt for libruby.so.2.0() so-name bump

* Sun Dec 22 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-10
- package must not obsolete itself
- improved indention

* Fri Dec 13 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-9
- fixed the way ruby(abi) is required
- dropped the symlinks in %%{ruby_vendorarchdir}, except for <= el6
- fixed directory ownerships on <= el6
- use BuildRequires: rubygems-devel on el6, too

* Tue Dec 10 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-8
- fixed symlinks in %%{ruby_vendorarchdir}

* Tue Dec 10 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-7
- adapted Requires: ruby(abi) = 1.9.1 for Fedora 18, only

* Tue Dec 10 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-6
- several improvements for RHEL <= 6 and added needed bits for RHEL <= 5
- added needed Provides

* Mon Nov 25 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-5
- Fedora <= 18 && RHEL <= 6 need Requires: ruby(abi)

* Mon Nov 25 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-4
- added conditional for Requires: ruby(release) or ruby(abi) on older dists

* Mon Oct 28 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-3
- added symlink to %%{gem_name}_ext.rb in %%{ruby_vendorarchdir}

* Sun Sep 15 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-2
- obsoleted common, common-devel and doc pkg
- moved some development-related files from main to devel pkg
- removed some unneeded files, e.g. the copy of sources inside %%{gem_instdir}

* Sat Sep 07 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0.8-1
- Initial rpm release (#1005463)
