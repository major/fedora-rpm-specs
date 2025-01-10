%global gem_name ncursesw

Name:           rubygem-%{gem_name}
Version:        1.4.11
Release:        4%{?dist}
Summary:        Ruby wrapper for the ncurses library, with wide character support
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://github.com/sup-heliotrope/ncursesw-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
Requires:       ruby
BuildRequires:  ruby
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc
# rubygem Requires/Provides are automatically generated in F21+
%if ! (0%{?fedora} >= 21 || 0%{?rhel} >= 8)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
This wrapper provides access to the functions, macros, global variables and 
constants of the ncurses library. These are mapped to a Ruby module named 
"Ncurses". Functions and external variables are implemented as singleton 
functions of the module Ncurses.

The ncursesw gem is a fork with improved wide character support.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
# examples are under a wide variety of licenses
# Automatically converted from old format: LGPLv2+ and MIT and MIT with advertising and LDPL - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-MIT-with-advertising AND LicenseRef-LDPL

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications/ .%{gem_dir}/doc/ %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/{lib,examples} %{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/

%files
%license COPYING
%doc README.md Changes THANKS TODO
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/examples

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.11-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.11-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 29 2024 Dan Callaghan <djc@djc.id.au> - 1.4.11-1
- upstream release 1.4.11, fixes build failure with GCC 14

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 1.4.10-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.10-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 1.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Dan Callaghan <djc@djc.id.au> - 1.4.10-1
- upstream release 1.4.10
- build steps updated to match current Ruby packaging conventions

* Mon Apr 13 2015 Dan Callaghan <dcallagh@redhat.com> - 1.4.9-1
- upstream release 1.4.9

* Mon Jan 27 2014 Dan Callaghan <dcallagh@redhat.com> - 1.4.3-1
- Initial package
