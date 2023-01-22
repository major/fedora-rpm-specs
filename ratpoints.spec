%global major	0

%ifarch %{ix86} x86_64
%global use_sse -DUSE_SSE
%else
%global use_sse %{nil}
%endif

Name:		ratpoints
Version:	2.1.3
Release:	28%{?dist}
Summary:	Find rational points on hyperelliptic curves
License:	GPLv2+
URL:		http://www.mathe2.uni-bayreuth.de/stoll/programs/
Source0:	http://www.mathe2.uni-bayreuth.de/stoll/programs/%{name}-%{version}.tar.gz
# Initially generated with help2man as:
# LD_LIBRARY_PATH=$PWD: help2man --section=1 --no-info \
#    --version-string="%%{version}" \
#    -o $RPM_BUILD_ROOT/%%{_mandir}/man1/ratpoints.1 ./ratpoints
# but edited for better formatting.
Source1:	%{name}.1
BuildRequires: make
BuildRequires:	gcc
BuildRequires:	gmp-devel
Patch0:		%{name}-shared.patch

%description
Ratpoints is a program that uses an optimized quadratic sieve algorithm
in order to find rational points on hyperelliptic curves.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Header and library for development with %{name}.

%prep
%autosetup -p1

sed -e "s|-Wall -O2 -fomit-frame-pointer|%{optflags} %{use_sse}|" \
   -e "s|-shared|& $RPM_LD_FLAGS|" \
   -i Makefile

%build
make %{?_smp_mflags}

%install
make install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT
install -p -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

%check
LD_LIBRARY_PATH=$PWD: make test

%files
%doc gpl-2.0.txt
%doc ratpoints-doc.pdf
%{_bindir}/ratpoints
%{_libdir}/libratpoints.so.%{major}
%{_mandir}/man1/ratpoints.1*

%files		devel
%{_includedir}/ratpoints.h
%{_libdir}/libratpoints.so

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-12
- Correct FTBFS in rawhide (#1239874)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 10 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-5
- Revert technically incorrect changes to silence rpmlint.
- Correct double install target in make command.

* Tue May 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-4
- Use %%name macro to follow package policy.
- Change hyperelliptic spelling to satisfy rpmlint.
- Move gpl-2.0.txt file to -devel package to provide documentation.

* Tue May 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-3
- Correct undefined symbols in the shared library.
- Link with RPM_LD_FLAGS to enable partial relro.

* Fri May 4 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-2
- Remove unneeded build requires.
- Prefer %%global over %%define. 
- Remove unneeded %%defattr from spec.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.3-1
- Initial ratpoints spec.
