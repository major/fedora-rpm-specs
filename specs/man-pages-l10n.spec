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
Version:        4.25.1
Release:        %autorelease
Summary:        Translated man pages from the Linux Documentation Project and other software projects

# original man pages are under various licenses, translations are GPL-3.0-or-later
# generated from upstream/fedora-rawhide/packages.txt with:
#   dnf --disablerepo=* --enablerepo=rawhide repoquery --queryformat "%%{license}\n" $(<upstream/fedora-rawhide/packages.txt) |\
#   (echo GPL-3.0-or-later && cat) |\
#   sort -u | sed -z 's/\n/ AND /g'
License:        Artistic Licence 2.0 and BSD and BSD with advertising and Copyright only and GFDL and GPL+ and GPLv2 and GPLv2+ and (GPLv2+ or Artistic) and GPLv2 with exceptions and GPLv2+ with exceptions and GPLv3+ and (GPLv3+ and BSD) and (GPLv3+ or BSD) and IJG and ISC and LGPLv2+ and LGPLv3+ and (LGPLv3+ or BSD) and MIT and psutils and Public Domain and Sendmail and Verbatim

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
