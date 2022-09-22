Name:           perl-Compress-Stream-Zstd
Version:        0.203
Release:        3%{?dist}
Summary:        Perl interface to the Zstd (Zstandard) (de)compressor
License:        BSD
URL:            https://metacpan.org/release/Compress-Stream-Zstd/
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-Stream-Zstd-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Unbundling is not possible, because libzstd-devel doesn't not contains
# 'compress/zstdmt_compress.h', which is used by lib/Compress/Stream/Zstd.xs 
Provides:       bundled(zstd) = 1.4.3


%description
The Compress::Stream::Zstd module provides an interface to the Zstd
(de)compressor.


%prep
%setup -q -n Compress-Stream-Zstd-%{version}


%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build


%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes README.md eg/
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Compress*
%{_mandir}/man3/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.203-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.203-2
- Perl 5.36 rebuild

* Mon May 09 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.203-1
- 0.203 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.202-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Xavier Bachelot <xavier@bachelot.org> 0.202-3
- More review fixes

* Thu Oct 21 2021 Xavier Bachelot <xavier@bachelot.org> 0.202-2
- Review fixes

* Thu Oct 07 2021 Xavier Bachelot <xavier@bachelot.org> 0.202-1
- Initial package
