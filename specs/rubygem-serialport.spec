%global gem_name serialport

Summary: Ruby library that provides a class for using RS-232 serial ports
Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 14%{?dist}
License: GPL-2.0-only
URL: http://github.com/hparra/ruby-serialport/ 
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Patch1: rubygem-serialport-c99.patch
BuildRequires: gcc
BuildRequires: ruby-devel
BuildRequires: rubygems-devel

%description
Ruby SerialPort is a class for using RS232 serial ports. It also contains 
low-level function to check current state of signals on the line. 

%package doc
BuildArch: noarch
Summary: Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
%patch -P 1 -p1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext

chmod a-x %{buildroot}%{gem_libdir}/serialport.rb


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/CHANGELOG
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/CHECKLIST
%exclude %{gem_instdir}/MANIFEST
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/CHANGELOG

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Alejandro Perez <aeperezt@fedoraproject.or> - 1.3.2-12
- Fix License expression
- Fix bump spec

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 1.3.2-9
- Fix C compatibility issue

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-3
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Alejandro Pérez <aeperezt@fedoraproject.org> - 1.3.2-1
- Initial package
