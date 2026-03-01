%global upstream_name manpages-l10n

%global distribution fedora-rawhide

%global translations \
    cs:    "Czech" \
    da:    "Danish" \
    de:    "German" \
    el:    "Greek" \
    es:    "Spanish" \
    fi:    "Finnish" \
    fr:    "French" \
    hu:    "Hungarian" \
    id:    "Indonesian" \
    it:    "Italian" \
    ko:    "Korean" \
    mk:    "Macedonian" \
    nl:    "Dutch" \
    nb:    "Norwegian Bokmål" \
    pl:    "Polish" \
    pt_BR: "Portuguese (Brazil)" \
    ro:    "Romanian" \
    ru:    "Russian" \
    sr:    "Serbian" \
    sv:    "Swedish" \
    uk:    "Ukrainian" \
    vi:    "Vietnamese"

Name:           man-pages-l10n
# Bumping epoch as a consequence of replacing man-pages-ru standalone package that has higher version (Obsoletes/Provides not needed)
# This is part of the Fedora 39 Change: https://fedoraproject.org/wiki/Changes/ManPagesRuRetirement
Epoch:          3
Version:        4.29.1
Release:        %autorelease
Summary:        Translated man pages from the Linux Documentation Project and other software projects

# original man pages are under various licenses, translations are GPL-3.0-or-later
# generated from upstream/fedora-rawhide/packages.txt with:
#   dnf --disablerepo=* --enablerepo=rawhide repoquery --queryformat "%%{license}\n" $(<upstream/fedora-rawhide/packages.txt) |\
#   (echo GPL-3.0-or-later && cat) |\
#   sort -u |\
#   awk '
#   NF { lines[++n] = $0 }
#   END {
#       print "%%{shrink:"
#       for (i = 1; i <= n; i++) {
#           line = lines[i]
#           if (line ~ / (AND|and) | (OR|or) /) line = "(" line ")"
#           line = "    " line (i < n ? " AND" : "")
#           tmp = line; if (gsub(/ (AND|and) | (OR|or) /, "&", tmp) > 2) {
#               gsub(/ (AND|and) /, " AND\n        ", line)
#               gsub(/ (OR|or) /, " OR\n        ", line)
#           }
#           print line
#       }
#       print "}"
#   }'
License:        %{shrink:
    AGPL-3.0-or-later AND
    Apache-2.0 AND
    (BSD-2-Clause AND
        BSD-3-Clause AND
        BSD-4.3TAHOE AND
        BSD-4-Clause-UC AND
        GPL-1.0-or-later AND
        GPL-2.0-only AND
        GPL-2.0-or-later AND
        LicenseRef-Fedora-Public-Domain AND
        LicenseRef-Fedora-UltraPermissive AND
        Linux-man-pages-1-para AND
        Linux-man-pages-copyleft AND
        Linux-man-pages-copyleft-2-para AND
        Linux-man-pages-copyleft-var AND
        MIT AND
        Spencer-94) AND
    (BSD-2-Clause-Darwin AND BSD-2-Clause) AND
    BSD-3-Clause AND
    (BSD-3-Clause AND
        BSD-2-Clause AND
        ISC AND
        SSH-OpenSSH AND
        ssh-keyscan AND
        sprintf AND
        LicenseRef-Fedora-Public-Domain AND
        X11-distribute-modifications-variant) AND
    (BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC) AND
    (BSD-3-Clause AND
        GPL-2.0-only AND
        LGPL-2.1-or-later AND
        GPL-3.0-or-later AND
        IJG AND
        MIT AND
        NTP AND
        PostgreSQL AND
        LicenseRef-MIT-CRL-Xim AND
        LicenseRef-Fedora-Public-Domain) AND
    (BSD-3-Clause AND GPL-2.0-or-later) AND
    (bsd-3-clause AND
        zlib AND
        licenseref-fedora-public-domain AND
        bsd-attribution-hpnd-disclaimer AND
        bsd-4.3tahoe AND
        bsd-4-clause-uc AND
        apache-2.0 AND
        lgpl-2.0-or-later AND
        (gpl-2.0-or-later OR
        bsd-2-clause OR
        bsd-3-clause OR
        bsd-4-clause) AND
        gpl-2.0-or-later AND
        xlock AND
        gpl-1.0-or-later AND
        mackerras-3-clause-acknowledgment AND
        mackerras-3-clause AND
        hpnd-fenneberg-Livingston AND
        sun-ppp AND
        hpnd-inria-imag AND
        sun-ppp-2000) AND
    (BSD-3-Clause-flex AND
        GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND
        GPL-3.0-or-later WITH Bison-exception-2.2 AND
        GPL-3.0-or-later WITH Texinfo-exception AND
        FSFAP AND
        FSFUL AND
        FSFULLR AND
        FSFULLRWD AND
        GPL-2.0-or-later AND
        X11) AND
    (BSD-3-Clause OR GPL-2.0-only) AND
    BSD-4-Clause AND
    BSD-4-Clause-UC AND
    (BSD-4-Clause-UC AND BSD-3-Clause) AND
    (BSD-4-Clause-UC AND GPL-2.0-or-later) AND
    EUPL-1.2 AND
    GPL-1.0-or-later AND
    (GPL-1.0-or-later AND LGPL-2.1-or-later) AND
    (GPL-1.0-or-later OR Artistic-1.0-Perl) AND
    ((GPL-1.0-or-later OR
        Artistic-1.0-Perl) AND
        Unicode-3.0 AND
        LicenseRef-Fedora-UltraPermissive) AND
    GPL-2.0-only AND
    (GPL-2.0-only AND GFDL-1.3-no-invariants-or-later) AND
    (GPL-2.0-only AND GPL-2.0-or-later) AND
    (GPL-2.0-only AND
        GPL-2.0-or-later AND
        BSD-3-Clause AND
        BSD-2-Clause AND
        (HPND-export-US-modify AND
        HPND-sell-variant) AND
        (GPL-2.0-only WITH Linux-syscall-note OR
        BSD-3-Clause)) AND
    (GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later) AND
    gpl-2.0-or-later AND
    GPL-2.0-or-later AND
    (GPL-2.0-or-later AND BSD-2-Clause) AND
    (GPL-2.0-or-later AND
        BSD-3-Clause AND
        BSD-2-Clause AND
        ISC AND
        LGPL-2.1-or-later) AND
    (GPL-2.0-or-later AND
        GPL-3.0-or-later AND
        FSFUL AND
        FSFULLRWD AND
        LGPL-2.1-only AND
        LGPL-2.1-or-later AND
        X11) AND
    (GPL-2.0-or-later AND
        GPL-3.0-or-later AND
        GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND
        GFDL-1.3-or-later AND
        FSFAP AND
        X11 AND
        LicenseRef-Fedora-Public-Domain) AND
    (GPL-2.0-or-later AND LGPL-2.1-or-later) AND
    (GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+) AND
    (GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain) AND
    (GPL-2.0-or-later AND LicenseRef-OFSFDL) AND
    (GPL-2.0-or-later AND NIST-PD) AND
    (GPL-2.0-or-later OR LGPL-2.1-or-later) AND
    (GPL-2.0-or-later WITH SANE-exception AND
        GPL-2.0-or-later AND
        GPL-2.0-only AND
        LGPL-2.0-or-later AND
        LGPL-2.1-or-later AND
        LicenseRef-Fedora-Public-Domain AND
        IJG AND
        MIT) AND
    (GPL-2.0-or-later WITH SANE-exception AND MIT) AND
    GPL-3.0-only AND
    (GPL-3.0-only and BSD-2-Clause) AND
    GPL-3.0-or-later AND
    (GPL-3.0-or-later AND
        BSD-3-Clause AND
        BSD-4.3TAHOE AND
        Latex2e-translated-notice) AND
    (GPL-3.0-or-later AND
        BSD-3-Clause AND
        FSFAP AND
        LGPL-2.1-or-later AND
        GPL-2.0-or-later AND
        LGPL-2.0-or-later AND
        LicenseRef-Fedora-Public-Domain AND
        GFDL-1.3-or-later AND
        LGPL-2.0-or-later WITH GCC-exception-2.0 AND
        GPL-3.0-or-later WITH GCC-exception-3.1 AND
        GPL-2.0-or-later WITH GNU-compiler-exception AND
        MIT) AND
    (GPL-3.0-or-later AND
        GFDL-1.3-no-invariants-or-later AND
        LGPL-2.1-or-later AND
        LGPL-3.0-or-later) AND
    (GPL-3.0-or-later AND GFDL-1.3-only) AND
    (GPL-3.0-or-later AND
        GFDL-1.3-or-later AND
        BSD-4-Clause-UC AND
        MIT AND
        X11 AND
        LicenseRef-Fedora-Public-Domain) AND
    (GPL-3.0-or-later AND GPL-2.0-or-later AND ISC) AND
    (GPL-3.0-or-later AND
        GPL-2.0-or-later AND
        LGPL-2.1-or-later AND
        BSD-3-Clause) AND
    (GPL-3.0-or-later AND
        (GPL-3.0-or-later AND
        BSD-4-Clause) AND
        (LGPL-3.0-or-later OR
        BSD-3-Clause) AND
        LGPL-2.0-or-later AND
        LGPL-3.0-or-later AND
        LicenseRef-Fedora-Public-Domain AND
        GFDL-1.3-or-later) AND
    (GPL-3.0-or-later AND
        GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND
        GPL-3.0-or-later WITH Bison-exception-2.2 AND
        GPL-2.0-or-later AND
        GPL-2.0-or-later WITH Autoconf-exception-generic AND
        LGPL-3.0-or-later AND
        LGPL-2.1-or-later AND
        LGPL-2.0-or-later AND
        FSFULLR AND
        GFDL-1.3-or-later AND
        X11) AND
    (GPL-3.0-or-later AND
        (GPL-3.0-or-later WITH Bison-exception-2.2) AND
        (LGPL-2.0-or-later WITH GCC-exception-2.0) AND
        BSD-3-Clause AND
        GFDL-1.3-or-later AND
        GPL-2.0-or-later AND
        LGPL-2.1-or-later AND
        LGPL-2.0-or-later) AND
    (GPL-3.0-or-later AND Latex2e) AND
    (GPL-3.0-or-later and LGPL-2.0-or-later) AND
    (GPL-3.0-or-later and LGPL-2.0-or-later and GFDL-1.2-or-later) AND
    (GPL-3.0-or-later AND
        LGPL-2.1-or-later AND
        GFDL-1.3-or-later AND
        FSFULLR) AND
    (GPL-3.0-or-later AND LGPL-3.0-or-later) AND
    (GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later) AND
    (GPL-3.0-or-later AND
        LGPL-3.0-or-later AND
        LGPL-2.1-or-later AND
        GPL-2.0-or-later AND
        LGPL-2.0-or-later AND
        GFDL-1.3-no-invariants-or-later) AND
    (GPL-3.0-or-later AND
        LicenseRef-Fedora-Public-Domain AND
        LGPL-2.1-or-later AND
        LGPL-3.0-only AND
        MIT) AND
    hdparm AND
    Info-ZIP AND
    LGPL-2.0-or-later AND
    (LGPL-2.0-or-later and GPL-3.0-or-later and GFDL-1.2-or-later) AND
    LGPL-2.1-only AND
    LGPL-2.1-or-later AND
    (LGPL-2.1-or-later AND MIT) AND
    (LGPL-2.1-or-later AND MIT AND GPL-2.0-or-later) AND
    LicenseRef-Callaway-BSD AND
    (LicenseRef-Callaway-BSD AND GPL-1.0-or-later) AND
    (LicenseRef-Callaway-BSD AND LicenseRef-Callaway-BSD-with-advertising) AND
    LicenseRef-Fedora-Public-Domain AND
    MIT-open-group AND
    Python-2.0.1 AND
    (sendmail-8.23 AND
        MIT AND
        MIT-CMU AND
        BSD-3-Clause AND
        CDDL-1.0 AND
        BSD-4-Clause AND
        BSD-4-Clause-UC AND
        PostgreSQL AND
        ISC AND
        HPND-sell-variant AND
        mailprio) AND
    Unlicense AND
    X11 AND
    X11-distribute-modifications-variant AND
    (X11-distribute-modifications-variant AND MIT-open-group)
}

URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n/
Source0:        https://salsa.debian.org/manpages-l10n-team/%{upstream_name}/-/archive/%{version}/%{upstream_name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  po4a


%description
Translated man pages from the Linux Documentation Project
and other software projects.


# generate subpackages
%{lua: for code, name in rpm.expand('%{translations}'):gmatch('(%S+):%s+(%b"")') do
    name = name:gsub('"', '')

    print('%package -n man-pages-' .. code .. '\n')
    print('Summary: ' .. name .. ' man pages from the Linux Documentation Project\n')
    print('Requires: man-pages-reader\n')
    print('Supplements: (man-pages and langpacks-' .. code .. ')\n')

    -- obsolete man-pages-es-extra
    if code == 'es' then
        print('Obsoletes: man-pages-es-extra < 1.55-36\n')
    end

    print('%description -n man-pages-' .. code .. '\n')
    print('Manual pages from the Linux Documentation Project, translated into ' .. name .. '.\n')
end}


%prep
%autosetup -p1 -n %{upstream_name}-%{version}


%build
%configure --enable-distribution=%{distribution}
%make_build


%install
%make_install
# prevent conflict with net-tools
rm %{buildroot}%{_mandir}/de/man5/ethers.5*

# generate %files sections
%{lua: for code in rpm.expand('%{translations}'):gmatch('(%S+):%s+%b""') do
    print('%files -n man-pages-' .. code .. '\n')
    print('%license LICENSE COPYRIGHT.md\n')
    print('%doc AUTHORS.md CHANGES.md README.md\n')
    print(rpm.expand('%{_mandir}') .. '/' .. code .. '/man*/*\n')
end}


%changelog
%autochangelog
