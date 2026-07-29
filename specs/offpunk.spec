# PyPI is still on 3.1
%bcond srht_source 1
%bcond tests 1

Name:           offpunk
Version:        3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Offline-First Gemini/Web/Gopher/RSS reader and browser

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        AGPL-3.0-or-later
URL:            https://offpunk.net/
%if %{with srht_source}
Source:         https://git.sr.ht/~lioploum/offpunk/archive/v%{version}.tar.gz#/offpunk-%{version}.tar.gz
%else
Source:         %{pypi_source offpunk}
%endif
Patch:          depend-on-beautifulsoup4-not-bs4.diff
Patch:          drop-dependency-on-file.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  gettext
# needed for both pyproject_check_import and tests
BuildRequires:  less
Requires:       file
Requires:       less
Requires:       python3dist(cryptography)
Requires:       xdg-utils
# web dependencies
Recommends:     chafa
Recommends:     curl
Recommends:     python3dist(beautifulsoup4)
Recommends:     python3dist(feedparser)
Recommends:     python3dist(readability)
# gopher dependencies
Recommends:     python3dist(charset-normalizer)
# nice to have
Recommends:     python3dist(setproctitle)
Recommends:     wl-clipboard



%global _description %{expand:
Offpunk is a command-line offline-first web browser for your terminal.

Every content you visit is cached and can be visited later while offline. If you
try to visit a content not available in your cache, it will be marked to be
downloaded later. Offpunk allows you to synchronise you computer once every
hour, day or week and work offline without being interrupted.

Offpunk transparently browse http/https/gemini/gopher/spartan/finger links. In
your terminal, it will nicely display HTML, Gemtext, Gophermap, txt, RSS, Atom
and even pictures. You can subscribe to an RSS feed or to any page. Offpunk
merges the concept of browsing pages and subscribing to feeds.}

%description %_description


%prep
%autosetup -p1 %{?with_srht_source:-n offpunk-v%{version}}


%generate_buildrequires
# individual features: better-tofu,chardet,html,http,process-title,rss
# full includes everything, see pyproject.toml
%pyproject_buildrequires -x full requirements.txt %{?with_tests:requirements-dev.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ansicat cert_migration netcache netcache_migration offblocklist offpunk offthemes offutils openk unmerdify xkcdpunk

%find_lang %{name}


%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif


%files -f %{pyproject_files} -f %{name}.lang
%{_bindir}/ansicat
%{_bindir}/netcache
%{_bindir}/offpunk
%{_bindir}/openk
%{_bindir}/unmerdify
%{_bindir}/xkcdpunk


%changelog
%autochangelog
