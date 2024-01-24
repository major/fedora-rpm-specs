Name:           npth
Version:        1.6
Release:        %autorelease
Summary:        The New GNU Portable Threads library
License:        LGPL-2.1-or-later
URL:            https://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
Source0:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2.sig
# Keyring generated from https://gnupg.org/devel/old-signature-keys.asc
Source2:        gpgkey-D8692123C4065DEA5E0F3AB5249B39D24F25E3B6.gpg
# Manual page is re-used and changed pth-config.1 from pth-devel package
Source3:        npth-config.1

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gnupg2

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%configure --disable-static
%make_build
# avoid multilib conflict
%ifarch x86_64 i686
sed -ie 's/".*-redhat-linux-gnu"/"$(uname -m)-redhat-linux-gnu"/' %{name}-config
sed -ie 's/libs=".* -lnpth/libs="-lnpth/' %{name}-config
sed -ie 's/Configured for: .*-redhat-linux-gnu/Configured for: x86_64+i686-redhat-linux-gnu/' src/%{name}.h
%endif

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 %{S:3}
find %{buildroot} -name '*.la' -delete -print

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LIB
%{_libdir}/lib%{name}.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_mandir}/man1/%{name}-config.1*
%{_datadir}/aclocal/%{name}.m4

%changelog
%autochangelog
