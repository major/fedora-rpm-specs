Name:           festival-freebsoft-utils
Version:        0.10
Release:        %autorelease
Summary:        Utilities that enhance Festival with some useful features

BuildArch:      noarch

License:        GPL-2.0-or-later
# The documentation is dual-licensed.
%global doc_license GPL-2.0-or-later OR GFDL-1.2-no-invariants-or-later
SourceLicense:  %{license} AND %{doc_license}
URL:            https://www.freebsoft.org/festival-freebsoft-utils
Source:         https://freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

# Fix a section level error in fdl.texi
# https://github.com/brailcom/festival-freebsoft-utils/pull/1
Patch:          https://github.com/brailcom/festival-freebsoft-utils/pull/1.patch

# We don’t actually need any of these to build, but BR’ing our runtime
# dependencies makes sure we don’t build a package that will fail to install.
BuildRequires:  festival
BuildRequires:  sox
BuildRequires:  /usr/bin/iconv

Requires:       festival
# From docs/festival-freebsoft-utils.texi:
#   Having SoX (@url{http://sox.sourceforge.net}) installed is strongly
#   recommended, many festival-freebsoft-utils functions don't work without it.
Recommends:     sox
# From docs/festival-freebsoft-utils.texi:
#   As Festival does not support UTF-8 encoding, festival-freebsoft-utils uses
#   the iconv utility for character coding conversions.
# Note that this is currently provided by glibc-common, so it should be
# available even without the explicit dependency.
Recommends:     /usr/bin/iconv

%description
A collection of utilities that enhance Festival with some useful features. They
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:

• Generalized concept of input events. festival-freebsoft-utils allows not only
  plain text synthesis, but also combining it with sounds. Additionally,
  mechanism of logical events mapped to other events is provided.
• Substitution of events for given words.
• High-level voice selection mechanism and setting of basic prosodic parameters.
• Spelling mode.
• Capital letter signalization.
• Punctuation modes, for explicit reading or not reading punctuation characters.
• Incremental synthesis of texts and events.
• Speech Dispatcher support.
• Rudimentary SSML support.
• Enhance the Festival extension language with functions commonly used in Lisp.
• Support for wrapping already defined Festival functions by your own code.
• Everything is written in the extension language, no patching of the Festival
  C++ sources is needed.


%package doc
Summary:        Documentation for festival-freebsoft-utils
License:        %{doc_license}

BuildRequires:  make
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

%description doc
Documentation for festival-freebsoft-utils in info, PDF, and HTML formats.


%prep
%autosetup -p1


%build
# Remove pre-built info page
%make_build clean
# Build info, PDF, and HTML docs from the texinfo sources.
%make_build info pdf html


%install
install -t '%{buildroot}/%{_datadir}/festival' -D -p -m 0644 *.scm
install -t '%{buildroot}/%{_infodir}' -D -p -m 0644 doc/*.info
install -t '%{buildroot}/%{_pkgdocdir}' -D -p -m 0644 \
    doc/*.pdf doc/*.html ANNOUNCE NEWS README


# Upstream does not provide any tests.


%files
%license COPYING
%{_datadir}/festival/*.scm


%files doc
%license COPYING
%doc %{_pkgdocdir}/ANNOUNCE
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/README

%doc %{_pkgdocdir}/festival-freebsoft-utils.pdf
%doc %{_pkgdocdir}/festival-freebsoft-utils.html

%doc %{_infodir}/festival-freebsoft-utils.info*


%changelog
%autochangelog
