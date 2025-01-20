Summary:        Reshape a data array
Name:           rs
Version:        20200313
Release:        8%{?dist}
# BSD-3-Clause (rs.c, rs.1), ISC (utf8.c, .linked/strtonum.c, reallocarray.c), MirOS (rs.h, check.pl)
License:        BSD-3-Clause AND ISC AND MirOS
URL:            https://man.openbsd.org/rs.1
Source0:        https://www.mirbsd.org/MirOS/dist/mir/%{name}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/MirBSD/mksh/bd8c18b7254d8735f18d239ca3fffaddc0434795/check.pl
BuildRequires:  gcc
BuildRequires:  perl-interpreter

%description
rs reads the standard input, interpreting each line as a row of blank-
separated entries in an array, transforms the array according to the
options, and writes it on the standard output. Numerous options control
input, reshaping and output processing; the simplest usage example is
"ls -1 | rs", which outputs the same (on an 80-column terminal) as the
modern "ls" with no "-1" argument.

%prep
%autosetup -p0 -n %{name}

%build
%{__cc} -DNEED_STRTONUM -I. -DMBSDPORT_H=\"rs.h\" -o %{name} $RPM_OPT_FLAGS $RPM_LD_FLAGS rs.c utf8.c .linked/strtonum.c

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%check
perl %{SOURCE1} -s check.t -v -p ./rs

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20200313-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200313-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200313-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200313-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 22 2023 Robert Scheck <robert@fedoraproject.org> 20200313-4
- Justify workarounds for Red Hat Enterprise Linux 7 (#2110814 #c3)

* Sat Sep 17 2022 Robert Scheck <robert@fedoraproject.org> 20200313-3
- Update license to SPDX expression

* Wed Jul 27 2022 Robert Scheck <robert@fedoraproject.org> 20200313-2
- Support for Red Hat Enterprise Linux 7 (thanks to Thorsten Glaser)

* Tue Jul 26 2022 Robert Scheck <robert@fedoraproject.org> 20200313-1
- Update to 20200313 (#2110814)
- Initial spec file for Fedora and Red Hat Enterprise Linux
