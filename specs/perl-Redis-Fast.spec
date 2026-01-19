Name:           perl-Redis-Fast
Version:        0.37
Release:        6%{?dist}
Summary:        Perl binding for Redis database
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Redis-Fast
Source0:        https://www.cpan.org/modules/by-module/Redis/Redis-Fast-%{version}.tar.gz

# https://salsa.debian.org/perl-team/modules/packages/libredis-fast-perl/-/raw/2112ad4f50b7293ff583a8f58f0ffb033a14de0f/debian/patches/remove-local-hiredis
Patch0:         perl-Redis-Fast-0.37-unbundle_hiredis.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  hiredis-devel >= 1.2.0
BuildRequires:  openssl-devel
BuildRequires:  valkey
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Module::Build::XSUtil) >= 0.02
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Run
BuildRequires:  perl(IO::Socket::SSL)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Parallel::ForkManager)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::UNIXSock)
BuildRequires:  perl(Time::HiRes) >= 1.77

ExcludeArch:    %{ix86}

%description
Redis::Fast is a wrapper around Salvatore Sanfilippo's hiredis C client. It
is compatible with Redis.pm.

%prep
%setup -q -n Redis-Fast-%{version}
# Drop bundled hiredis
%patch -P0 -p1
rm -vr deps/

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset REDIS_DEBUG
unset REDIS_SERVER
export REDIS_SERVER_PATH=/usr/bin/valkey-server
unset TEST_REDIS_SERVER_SOCK_PATH
unset USE_SSL
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorarch}/auto/Redis/
%{perl_vendorarch}/Redis/
%{_mandir}/man3/Redis::Fast*.3pm*

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Oct 17 2025 Xavier Bachelot <xavier@bachelot.org> - 0.37-5
- Drop conditional around ExcludeArch, no i686 valkey build anywhere
- Directly BR: valkey rather than valkey-compat-redis
- Drop duplicate BR:

* Thu Oct 16 2025 Xavier Bachelot <xavier@bachelot.org> - 0.37-4
- Drop some useless BR:s after hiredis unbundling
- Escape percent sign in changelog

* Wed Oct 15 2025 Xavier Bachelot <xavier@bachelot.org> - 0.37-3
- Add BR: gcc
- Add ExcludeArch: %%{ix86} for 44+, where valkey is missing for i686
- Unset test envars

* Wed Oct 15 2025 Xavier Bachelot <xavier@bachelot.org> - 0.37-2
- Unbundle hiredis
- Review fixes

* Mon Apr 14 2025 Xavier Bachelot <xavier@bachelot.org> - 0.37-1
- Initial specfile
