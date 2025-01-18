Name: bcftools
Version: 1.15.1
Release: 11%{?dist}
Summary: Tools for genomic variant calling and manipulating VCF/BCF files

# This software is available under a choice of one of two licenses,
# the MIT/Expat (MIT) or the GNU General Public License Version 3
# (GPL-3.0-or-later).
# And if compiled with the GNU Scientific Library, in this case it is built
# with --enable-libgsl, the use of this software is governed by the
# GPL-3.0-or-later license.
# See <https://github.com/samtools/bcftools/blob/develop/LICENSE>.
License: GPL-3.0-or-later
# https:// is better than http://.
URL: https://www.htslib.org/
Source0: https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Fix test_vcf_plugin tests.
# https://github.com/samtools/bcftools/commit/0676ccfb710778129f0337aa4ea3fa014f7c97fb
Patch0: bcftools-1.15.1-aarch64-fix-vcf_plugin-tests.patch

BuildRequires: gcc
BuildRequires: gsl-devel
BuildRequires: htslib-devel
BuildRequires: htslib-tools
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: zlib-devel
BuildRequires: make
# bcftools had been included in samtools version 0.X.
# https://github.com/samtools/samtools/commit/e7ae7f96c7e78a2dd6eabdaed57037c483951929
Conflicts: samtools < 1.0
# A big-endian (s390x) environment is not supported.
# https://github.com/samtools/htslib/issues/355
ExcludeArch: s390x

%description
BCFtools is a set of utilities that manipulate genomic variant calls in the
Variant Call Format (VCF) and its binary counterpart (BCF). All commands work
transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.

(This BCFtools includes the polysomy subcommand, which is implemented using
the GNU Scientific Library. Hence this package is licensed according to the
GNU General Public License, rather than the MIT license used when BCFtools
is built without the polysomy subcommand.)


%prep
%setup -q
%patch -P0 -p1

sed -i '1s|/usr/bin/env perl|/usr/bin/perl|' misc/*.pl misc/plot-vcfstats
sed -i '1s|/usr/bin/env python3\{0,1\}|%{__python3}|' misc/*.py


%build
%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
  --prefix=%{_prefix} \
  --with-htslib=system \
  --enable-perl-filters \
  --enable-libgsl \
  --with-bcf-plugin-path='%{_usr}/local/libexec/bcftools:$(plugindir)'
%make_build


%install
%make_install


%check
# Check if bcftools is built with system htslib.
ldd bcftools | grep -E '/lib(64)?/libhts\.so\.'

%ifarch i686
# Skip 2 failed tests.
# https://github.com/samtools/bcftools/issues/1776
sed -i -E '/^test_vcf_convert_hs2vcf.+convert.gs.gt.ids.3N6.gen.+/ s/^/#/' test/test.pl
%endif
make test


%files
%doc AUTHORS NEWS
%license LICENSE
# We do not use a wildcard to list bin files, because this often leads
# to problems when the name changes or something additional is installed.
%{_bindir}/bcftools
%{_bindir}/color-chrs.pl
%{_bindir}/gff2gff.py
%{_bindir}/guess-ploidy.py
%{_bindir}/plot-roh.py
%{_bindir}/plot-vcfstats
%{_bindir}/run-roh.pl
%{_bindir}/vcfutils.pl
%{_libexecdir}/bcftools
%{_mandir}/man1/bcftools.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.15.1-9
- Perl 5.40 rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Benson Muite <benson_muite@emailplus.org> - 1.15.1-6
- Use SPDX license identifier

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.15.1-4
- Perl 5.38 rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.15.1-2
- Rebuild for gsl-2.7.1

* Mon Aug 15 2022 Jun Aruga <jaruga@redhat.com> - 1.15.1-1
- Update to BCFtools version 1.15.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-3
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 John Marshall <jmarshall@hey.com> - 1.13-1
- Update to BCFtools version 1.13
- Remove outdated patches which have been applied upstream
- Update Python shebang rewriting to handle both "python" and "python3"
- Package gff2gff.py script, added in BCFtools 1.11

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-7
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-4
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jun Aruga <jaruga@redhat.com> - 1.9-3
- Fix the build failure adding perl(FindBin) build dependency.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Jun Aruga <jaruga@redhat.com> - 1.9-1
- Exclude a CPU architecture s390x.
- Add Conflicts tag for samtools < 1.0.
- Align the field delimiter as 1 space.
- Use additional RPM macros for Source0.
- Add a logic to check if bcftools is built with system htslib.
- Update comments for license.

* Wed Nov 06 2019 John Marshall <jmarshall@users.sourceforge.net> - 1.9-1
- New spec file for bcftools, now separate from samtools (#1767792).
- Backported Python 3 and configure patches from later upstream development.
