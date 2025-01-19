Name:           perl-Compress-Stream-Zstd
Version:        0.206
Release:        8%{?dist}
Summary:        Perl interface to the Zstd (Zstandard) (de)compressor
License:        BSD-2-Clause AND BSD-3-Clause
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
# Unbundling is not possible, because libzstd-devel doesn't not contains
# 'compress/zstdmt_compress.h', which is used by lib/Compress/Stream/Zstd.xs 
Provides:       bundled(zstd) = 1.5.5


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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.206-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.206-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.206-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.206-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.206-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.206-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.206-2
- Perl 5.38 rebuild

* Mon Jun 05 2023 Xavier Bachelot <xavier@bachelot.org> 0.206-1
- Update to 0.206 (RHBZ#2168705)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
