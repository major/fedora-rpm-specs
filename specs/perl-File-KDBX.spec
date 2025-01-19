# File::KeePass::KDBX is needed for a test but it requires ourselves.
# Once this is added to Fedora, change this to bcond_without and rebuild.
%bcond_with file-keepass-kdbx

# Optional packages not yet in Fedora:
%bcond_with pass-otp
%bcond_with posix-1003
%bcond_with file-kdbx-xs
%bcond_with crypt-stream-serpent
%bcond_with crypt-stream-twofish

# Only required for 32-bit Perl:
%bcond_with math-bigint

Name:		perl-File-KDBX
Version:	0.906
Release:	10%{?dist}
Summary:	Encrypted database to store secret text and files

License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-KDBX
Source0:	https://cpan.metacpan.org/authors/id/C/CC/CCM/File-KDBX-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl(:VERSION) >= 5.010
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Errno)
BuildRequires:	perl(ExtUtils::MakeMaker)
# ---------- Test Requires ----------
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Std)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
%if 0%{?with_math-bigint}
BuildRequires:	perl(Math::BigInt) >= 1.993
%endif
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 1.001004_001
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(blib)
BuildRequires:	perl(lib)
BuildRequires:	perl(utf8)
# ---------- Test Recommends ----------
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(File::KeePass)
%if 0%{?with_file-keepass-kdbx}
BuildRequires:	perl(File::KeePass::KDBX)
%endif
%if 0%{?with_pass-otp}
BuildRequires:	perl(Pass::OTP)
%endif
# ---------- Test Suggests ----------
%if 0%{?with_posix-1003}
BuildRequires:	perl(POSIX::1003)
%endif
# ---------- Runtime Requires ----------
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Crypt::Argon2)
BuildRequires:	perl(Crypt::Cipher)
BuildRequires:	perl(Crypt::Cipher::AES)
BuildRequires:	perl(Crypt::Digest)
BuildRequires:	perl(Crypt::Mac::HMAC)
BuildRequires:	perl(Crypt::Misc) >= 0.049
BuildRequires:	perl(Crypt::Mode::CBC)
BuildRequires:	perl(Crypt::PRNG)
BuildRequires:	perl(Crypt::Stream::ChaCha) >= 0.048
BuildRequires:	perl(Crypt::Stream::Salsa20) >= 0.055
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Hash::Util::FieldHash)
#Duplicated above: BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Cmd) >= 0.84
BuildRequires:	perl(Iterator::Simple)
BuildRequires:	perl(List::Util) >= 1.33
#Duplicated above: BuildRequires:	perl(Math::BigInt) >= 1.993
BuildRequires:	perl(Module::Load)
BuildRequires:	perl(Module::Loaded)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Ref::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl(Time::Local) >= 1.19
BuildRequires:	perl(Time::Piece) >= 1.33
BuildRequires:	perl(XML::LibXML)
BuildRequires:	perl(XML::LibXML::Reader)
BuildRequires:	perl(boolean)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(overload)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# ---------- Runtime Recommends ----------
BuildRequires:	perl(B::COW)
BuildRequires:	perl(Compress::Raw::Zlib)
%if 0%{?with_file-kdbx-xs}
BuildRequires:	perl(File::KDBX::XS)
%endif
#Duplicated above: BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Compress::Gzip)
BuildRequires:	perl(IO::Uncompress::Gunzip)
#Duplicated above: BuildRequires:	perl(Pass::OTP)
# ---------- Runtime Suggests ----------
%if 0%{?with_crypt-stream-serpent}
BuildRequires:	perl(Crypt::Stream::Serpent)
%endif
%if 0%{?with_crypt-stream-twofish}
BuildRequires:	perl(Crypt::Stream::Twofish)
%endif

## ---------- Requires not found automatically ----------
Recommends:	perl(B::COW)
Requires:	perl(Carp)
Requires:	perl(Compress::Raw::Zlib)
Requires:	perl(Config)
Requires:	perl(Crypt::Cipher::AES)
Requires:	perl(Crypt::Stream::ChaCha) >= 0.048
Requires:	perl(Crypt::Stream::Salsa20) >= 0.055
Requires:	perl(Data::Dumper)
##For Tests Only: Requires:	perl(File::Spec)
Requires:	perl(File::Temp)
Requires:	perl(IO::Compress::Gzip)
Requires:	perl(IO::Uncompress::Gunzip)
%if 0%{?with_math-bigint}
Requires:	perl(Math::BigInt) >= 1.993
%endif
Requires:	perl(Scope::Guard)
Requires:	perl(Text::ParseWords)
##Not sure why: Requires:	perl(Time::Local) >= 1.19

%{?perl_default_filter}

%description
File::KDBX provides everything you need to work with KDBX databases. A KDBX
database is a hierarchical object database which is commonly used to store
secret information securely. It was developed for the KeePass password
safe.


%prep
%autosetup -p1 -n File-KDBX-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%make_build test


%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/KDBX.pm
%{perl_vendorlib}/File/KDBX/
%{_mandir}/man3/File::KDBX*3pm*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.906-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.906-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.906-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.906-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-6
- Simplify the %%files list to not list every single file individually
- Add some missing BR and Requires

* Tue Sep 26 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-5
- Use cpan.metacpan.org as the Source0 URL
- Drop __perl macro in favor of straight perl
- Add NO_PACKLIST=1 NO_PERLLOCAL=1 to 'perl MakeFile.PL ...'
- Drop the 2 find's in %%install
- Replace 'make pure_install ...' with %%make_install
- Use %%make_build in %%check
- Be more specific in %%files list

* Mon Sep 18 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-4
- Switch to bcond_with for all optional requirements

* Sun Sep 17 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-3
- Cleanup and document BuildRequires/Requires

* Fri Sep 15 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-2
- Add bcond bootstrap macro that excludes BR: perl-File-KeePass-KDBX

* Sat May 20 2023 Charles R. Anderson <cra@alum.wpi.edu> - 0.906-1
- Specfile autogenerated by cpanspec 1.78 and modified by cra.
