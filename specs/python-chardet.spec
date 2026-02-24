Name:           python-chardet
Version:        5.2.0
Release:        %autorelease
Summary:        Python character encoding detector

# The entire source, after tests/ are filtered, is LGPL-2.1-or-later. See the
# comment above Source0 for more details on tests/.
License:        LGPL-2.1-or-later
URL:            https://github.com/chardet/chardet
# A filtered source tarball, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because the contents of tests/ are under various undocumented
# licenses and are, for the most part, not freely redistributable. See:
#
#   problematic licensing of /tests?
#   https://github.com/chardet/chardet/issues/231
Source0:        chardet-%{version}-filtered.tar.zst
Source1:        get_source
# Hand-written for Fedora in groff_man(7) format based on --help output
Source2:        chardetect.1

BuildSystem:            pyproject
BuildOption(install):   -l chardet

BuildArch:      noarch

%global common_description %{expand:
Chardet: The Universal Character Encoding Detector

Detects:

  • ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
  • Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified
    Chinese)
  • EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
  • EUC-KR, ISO-2022-KR, Johab (Korean)
  • KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
  • ISO-8859-5, windows-1251 (Bulgarian)
  • ISO-8859-1, windows-1252 (Western European languages)
  • ISO-8859-7, windows-1253 (Greek)
  • ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
  • TIS-620 (Thai)

ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
disabled.}

%description
%{common_description}


%package -n python3-chardet
Summary:        %{summary}

# Removed in F41; keep the upgrade path through F43:
Obsoletes:      python-chardet-doc < 5.2.0-12

%description -n python3-chardet
%{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE2}'


# We cannot run the upstream tests because they would require data files with
# problematic license status.


%files -n python3-chardet -f %{pyproject_files}
%doc README.rst
%{_bindir}/chardetect
%{_mandir}/man1/chardetect.1*


%changelog
%autochangelog
