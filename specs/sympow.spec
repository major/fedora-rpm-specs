Name:           sympow
Version:        2.023.6
Release:        12%{?dist}
Summary:        Special Values of Symmetric Power Elliptic Curve L-Functions

# The License tag is a lie.  See
# https://gitlab.com/rezozer/forks/sympow/-/issues/7
License:        BSD-2-Clause AND GPL-2.0-or-later
URL:            https://gitlab.com/rezozer/forks/sympow
Source0:        https://gitlab.com/rezozer/forks/sympow/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# Do not try to create the cachedir; RPM already created it
Patch0:         sympow-2.023.5-cachedir.patch
# Upstream patch to fix a crash
# https://gitlab.com/rezozer/forks/sympow/-/merge_requests/4
Patch1:         sympow-2.023.6-crash.patch
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pari-gp

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Requires:       %{name}-data = %{version}-%{release}
Requires:       grep
Requires:       pari-gp
Requires:       sed

%description
SYMPOW is a program for computing special values of symmetric power
elliptic curve L-functions.

%package        data
Summary:        Shared data for sympow
BuildArch:      noarch

%description    data
This package provides the essential SYMPOW architecture-independent
material, namely shared data and scripts.


%prep
%autosetup -p1 -n %{name}-v%{version}


%build
export PREFIX="%{_prefix}"
./Configure

# Do not override Fedora flags
sed -i 's/-O3 //' Makefile

# Put the helper script in a canonical place
cat >> config.h << EOF
#define PKGLIBDIR "%{_libexecdir}/%{name}"
EOF
sed -i 's,%{_prefix}/lib/%{name},%{_libexecdir}/%{name},' Makefile

%make_build


%install
%make_install
mkdir -p %{buildroot}%{_var}/cache/%{name}

# The install step creates the txt files, so we cannot convert them to bin
# files until now.
mkdir -p binfiles/$(config/endiantuple)
for fil in datafiles/*.txt; do
  NUM=$(grep -Fc AT ${fil} || :)
  if [ "$NUM" -gt 0 ]; then
    ./sympow -txt2bin $NUM binfiles/$(config/endiantuple)/$(basename ${fil/txt/bin}) < $fil
  fi
done
chmod 0644 binfiles/$(config/endiantuple)/*.bin
cp -a binfiles %{buildroot}%{_var}/cache/%{name}/datafiles


%files
%doc HISTORY README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_var}/cache/%{name}/

%files data
%license COPYING
%{_datadir}/%{name}/
%{_libexecdir}/%{name}/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 2.023.6-9
- Stop building for 32-bit x86

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 2.023.6-7
- Add upstream patch to prevent a crash
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  9 2020 Jerry James <loganjerry@gmail.com> - 2.023.6-1
- Update to 2.023.6
- Drop upstreamed -f-no-common patch
- Fix installation path for the binary files

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jerry James <loganjerry@gmail.com> - 2.023.5-3
- Add -f-no-common patch to fix FTBFS with gcc 10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.023.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Jerry James <loganjerry@gmail.com> - 2.023.5-1
- Update to 2.023.5
- Change URLs to new upstream location
- Drop upstreamed -datafiles patch
- Use license macro
- Make a noarch subpackage to hold the data files

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.019-6
- Remove BuildRoot, %%clean and %%defattr.
- Add my Mandriva patch to create .bin files otherwise sympow will
  just crash on actual usage.
- Remove sympow-launcher and create it dynamically in spec.
- The new sympow launcher also checks for the SYMPOW_DATA environment
  variable and copies data there if empty. This is required because
  data files may be changed or new ones created by users.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 1.019-2
- Make launcher-script multilibs-safe.

* Sun Dec 14 2008 Conrad Meyer <konrad@tylerc.org> - 1.019-1
- Initial package.
