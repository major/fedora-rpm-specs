%global         gem_name ruby-shadow

Name:           rubygem-%{gem_name}
Version:        2.5.1
Release:        10%{?dist}
Summary:        Ruby shadow password module
License:        LicenseRef-Fedora-UltraPermissive OR Unlicense
URL:            https://github.com/apalmblad/ruby-shadow
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://raw.githubusercontent.com/apalmblad/ruby-shadow/master/test/basic_test.rb
# https://github.com/apalmblad/ruby-shadow/pull/29
# Ruby3.2 completely removes taintedness function
Patch0:         ruby-shadow-2.5.1-taintedness-ruby32-removal.patch
# https://github.com/apalmblad/ruby-shadow/pull/31
# Ruby3.2 mkmf CONFIG uses reference for other variables yet more
Patch1:         ruby-shadow-2.5.1-extconf-ruby32-fix.patch
Patch2:         ruby-shadow-2.5.1-cflags.patch
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
Obsoletes:      ruby-shadow < 1.4.1-36
Provides:       ruby-shadow = %{version}-%{release}
Provides:       ruby(shadow) = %{version}
%description
This module provides access to shadow passwords on Linux and Solaris.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep
%autosetup -p1 -n  %{gem_name}-%{version}
cp %{SOURCE1} .

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror=implicit-function-declaration'"
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# two identical so files confuses rpmbuild
find %{buildroot}%{gem_dir}/ -name \*.so -delete

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
cp %{SOURCE1} .%{gem_instdir}
pushd .%{gem_instdir}
if [ $(id -u) = 0 ]; then
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)'
else
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)' || :
fi
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/*
%doc %{gem_instdir}/HISTORY
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.euc

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.1-10
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-8
- Use autosetup macro

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.1-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Thu Dec  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.1-2
- Backport upstream pull request for ruby3.2 build issue
- Add -Werror=implicit-function explicitly to detect such function

* Thu Dec  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.1-1
- 2.5.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-11
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-7
- Add C compiler

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.5.0-4
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-3
- F-28: rebuild for ruby25

* Mon Oct 09 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-2
- Remove group
- Run tests

* Thu Oct 05 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-1
- 2.5.0
- Remove non Fedora support
- Simplify

* Fri Mar 01 2013 Moses Mendoza <moses@puppetlabs.com> - 2.2.0-1
- Update to upstream 2.2.0
- Move gem path macro definitions inside rhel5 macro block
- Install only files we want rather than removing files we dont
- Remove extraneous case in spec for gem_instdir/*.so
- Move gemspec(s) into docs package

* Mon Nov 05 2012 Moses Mendoza <moses@puppetlabs.com> - 2.1.4-1
- Update to 2.1.4
- Dynamically define gem_dir macro
- Use ruby_sitearch macro for EPEL, fedora < 17

* Tue Apr 17 2012 Todd Zullinger <tmz@pobox.com> - 2.1.3-2
- Use gem_extdir macro on F-17 and above

* Fri Apr 06 2012 Todd Zullinger <tmz@pobox.com> - 2.1.3-1
- Update to 2.1.3
- Fix license tag

* Sun Apr 01 2012 Todd Zullinger <tmz@pobox.com> - 2.1.2-3
- Revert gem repacking until ruby guidelines are finalized
- Only define gem macros for EPEL, all Fedora releases have them
- Add BuildRoot and clean it manually for EL-5

* Thu Feb 16 2012 Todd Zullinger <tmz@pobox.com> - 2.1.2-2
- Minor cleanups for review
- Changes for building on EL-6 (EL-5s rubygems is too old)

* Mon Jan 16 2012 Michael Stahnke <mastahnke@gmail.com> - 2.1.2-1
- Initial package
