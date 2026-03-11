# Version 6.0.0 had __version__ = "6.0.0dev0" in chardet/version.py. A
# follow-up commit fixed this, updating the version to "6.0.0.post1", and was
# released on PyPI as 6.0.0.post1, but no corresponding tag was pushed to
# GitHub. We package from the commit; we don’t put snapshot information in the
# Version because we know that this commit does correspond to the 6.0.0.post1
# release.
%global commit 2fa72d84fdb9cb926eb1e7e40230a33b1dd81bb8

Name:           python-chardet
Version:        6.0.0.post1
Release:        %autorelease
Summary:        Python character encoding detector

# The entire source, after tests/ are filtered, is LGPL-2.1-or-later. See the
# comment above Source0 for more details on tests/.
License:        LGPL-2.1-or-later
URL:            https://github.com/chardet/chardet
# A filtered source tarball, obtained by (see Source1):
#
#   ./get_source %%{version}
# or
#   ./get_source %%{commit}
#
# is required because the contents of tests/ are under various undocumented
# licenses and are, for the most part, not freely redistributable. See:
#
#   problematic licensing of /tests?
#   https://github.com/chardet/chardet/issues/231
# Source0:        chardet-%%{version}-filtered.tar.zst
Source0:        chardet-%{commit}-filtered.tar.zst
Source1:        get_source
# Hand-written for Fedora in groff_man(7) format based on --help output
Source2:        chardetect.1

BuildSystem:            pyproject
BuildOption(install):   -l chardet

BuildArch:      noarch

%global common_description %{expand:
Chardet: The Universal Character Encoding Detector

Detects over 70 character encodings including:

  • All major Unicode encodings (UTF-8, UTF-16, UTF-32)
  • Windows code pages (Windows-1250 through Windows-1258)
  • ISO-8859 family (ISO-8859-1 through ISO-8859-16)
  • CJK encodings (Big5, GB18030, EUC-JP, EUC-KR, Shift-JIS, and more)
  • Cyrillic encodings (KOI8-R, KOI8-U, IBM866, and more)
  • Mac encodings (MacRoman, MacCyrillic, and more)
  • DOS/OEM code pages (CP437, CP850, CP866, and more)
  • EBCDIC variants (CP037, CP500)}

%description
%{common_description}


%package -n python3-chardet
Summary:        %{summary}

%description -n python3-chardet
%{common_description}


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


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
