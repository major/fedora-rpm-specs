Name:		msmtp
Version:	1.8.22
Release:	%autorelease
Summary:	SMTP client
License:	GPLv3+
URL:		https://marlam.de/msmtp/
Source0:	https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz
Source1:	https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz.sig
Source2:	https://marlam.de/key.txt

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	libidn-devel
BuildRequires:	libgsasl-devel
BuildRequires:	libsecret-devel
BuildRequires:	make
# for %%gpgverify
BuildRequires:	gnupg2

Requires(post):		%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives

%description
It forwards messages to an SMTP server which does the delivery.
Features include:
  * Sendmail compatible interface (command line options and exit codes).
  * Authentication methods PLAIN,LOGIN,CRAM-MD5,DIGEST-MD5,GSSAPI,and NTLM
  * TLS/SSL both in SMTP-over-SSL mode and in STARTTLS mode.
  * Fast SMTP implementation using command pipe-lining.
  * Support for Internationalized Domain Names (IDN).
  * DSN (Delivery Status Notification) support.
  * RMQS (Remote Message Queue Starting) support (ETRN keyword).
  * IPv6 support.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -ivf
%configure --disable-rpath --with-libsecret --with-libgsasl
%make_build

%install
%make_install
%find_lang %{name}
rm -f scripts/Makefile*
rm -f %{buildroot}%{_infodir}/dir

# setup dummy files for alternatives
touch %{buildroot}%{_bindir}/msmtp

%post
%{_sbindir}/update-alternatives --install %{_sbindir}/sendmail mta %{_bindir}/msmtp 40 \
  --slave %{_prefix}/lib/sendmail mta-sendmail %{_bindir}/msmtp \
  --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/msmtp.1.gz \
  --slave %{_bindir}/mailq mta-mailq %{_bindir}/msmtp \
  --slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/msmtp.1.gz

%postun
if [ $1 -eq 0 ] ; then
	%{_sbindir}/update-alternatives --remove mta %{_bindir}/msmtp
fi

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS scripts
%doc doc/msmtprc-system.example doc/msmtprc-user.example
%{_bindir}/%{name}*
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}*.1*

%changelog
%autochangelog
