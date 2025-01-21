Summary:	Mail filter for Sender Policy Framework verification
Name:		smf-spf
Version:	2.5.1^20220423g061e937
Release:	5%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/jcbf/smf-spf/
Source0:	https://github.com/jcbf/smf-spf/archive/061e9371f761f70afd40af349f4037fe0460725c.zip
Source1:	smf-spf.service
Source2:	README.rpm
Source3:	smf-spf.sysusers
Source4:	smfs.conf

# Use the distribution optimization flags and don't strip the binary,
# so we get usable debuginfo
Patch0:		smf-spf-2.5.1-Makefile.patch

# Tag failing messages by default rather than rejecting them
Patch2:		smf-spf-2.5.1-conf.patch

# Use /run rather than /var/run with systemd
Patch5:		smf-spf-2.5.1-rundir.patch

BuildRequires:	libspf2-devel >= 1.2.5
BuildRequires:	sendmail-milter-devel >= 8.12
BuildRequires:	systemd-rpm-macros
BuildRequires:	make gcc coreutils
%{?sysusers_requires_compat}

Requires:	sendmail >= 8.12

%description
smf-spf is a lightweight, fast and reliable Sendmail milter that implements the
Sender Policy Framework technology with the help of the libspf2 library. It
checks SPF records to make sure that e-mail messages are authorized by the
domain that it is coming from. It's an alternative for the spfmilter,
spf-milter, and milter-spiff milters.

%prep
%autosetup -n %{name}-061e9371f761f70afd40af349f4037fe0460725c/

# Copy in additional sources
install -m 0644 %{SOURCE1} .
install -m 0644 %{SOURCE2} .
install -m 0644 %{SOURCE3} .
install -m 0644 %{SOURCE4} .

%build
%make_build OPTFLAGS="%{optflags}" LDFLAGS="%{build_ldflags} -lmilter -lpthread -lspf2"

%install
install -d -m 700 %{buildroot}/run/smfs
install -Dp -m 755 smf-spf %{buildroot}%{_sbindir}/smf-spf
install -Dp -m 644 smf-spf.conf %{buildroot}%{_sysconfdir}/mail/smfs/smf-spf.conf
# Install systemd unit file and tmpfiles.d configuration for /run/smfs
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/smf-spf.service
install -Dp -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/smfs.conf

# Create dummy socket for %%ghost-ing
: > %{buildroot}/run/smfs/smf-spf.sock

%pre
%sysusers_create_compat %{SOURCE3}

%post
%systemd_post smf-spf.service

%preun
%systemd_preun smf-spf.service

%postun
%systemd_postun_with_restart smf-spf.service

%files
%doc ChangeLog readme README.rpm
%license COPYING
%{_sbindir}/smf-spf
%dir %{_sysconfdir}/mail/smfs/
%config(noreplace) %{_sysconfdir}/mail/smfs/smf-spf.conf
%attr(0700,smfs,smfs) %dir /run/smfs/
%ghost %attr(0600,smfs,smfs) /run/smfs/smf-spf.sock
%{_unitdir}/smf-spf.service
%{_tmpfilesdir}/smfs.conf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1^20220423g061e937-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1^20220423g061e937-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1^20220423g061e937-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1^20220423g061e937-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Jordi Sanfeliu <jordi@fibranet.cat> 2.5.1^20220423g061e937-1
- Updated build process.

* Thu Nov 19 2020 Jordi Sanfeliu <jordi@fibranet.cat> 2.5.1-1
- Updated to 2.5.1.

* Sun Jul 28 2013 Paul Howarth <paul@city-fan.org> 2.0.2-6
- Systemd detection was broken in F-19 so hardcode it instead

* Tue Jul  3 2012 Paul Howarth <paul@city-fan.org> 2.0.2-5
- Move tmpfiles.d config from %%{_sysconfdir} to %%{_prefix}/lib
- Delay start-up until after network

* Thu Sep 29 2011 Paul Howarth <paul@city-fan.org> 2.0.2-4
- Use presence of /run/lock to determine if init is systemd

* Wed Jul 13 2011 Paul Howarth <paul@city-fan.org> 2.0.2-3
- Switch to systemd configuration where appropriate
- Nobody else likes macros for commands

* Wed Jul 28 2010 Paul Howarth <paul@city-fan.org> 2.0.2-2
- Modernize initscript and scriptlets
- Add dist tag

* Thu Jan 11 2007 Paul Howarth <paul@city-fan.org> 2.0.2-1
- Update to 2.0.2
- Failing mails now tagged [SPF:fail] by default instead of [SPF-FAIL]

* Fri Sep 22 2006 Paul Howarth <paul@city-fan.org> 2.0.1-1
- Update to 2.0.1

* Thu Sep 21 2006 Paul Howarth <paul@city-fan.org> 2.0.0-1
- Initial RPM build
