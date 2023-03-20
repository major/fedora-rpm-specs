Name:       buku
Version:    4.8
Release:    %autorelease
Summary:    Powerful command-line bookmark manager

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/Buku
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     buku-fix-makefile.patch

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(certifi)
Requires:       python3dist(cryptography)
Requires:       python3dist(html5lib)
Requires:       python3dist(urllib3)

%description
Buku is a powerful bookmark manager written in Python3 and SQLite3.

Buku fetches the title of a bookmarked web page and stores it along
with any additional comments and tags. You can use your favourite editor
to compose and update bookmarks. With multiple search options, including regex
and a deep scan mode (particularly for URLs), it can find any bookmark
instantly. Multiple search results can be opened in the browser at once.

%prep
%autosetup -p1

%build
# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%make_install PREFIX=%{_prefix}

install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/buku-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/buku.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_buku

%py3_shebang_fix %{buildroot}%{_bindir}

%files
%doc CHANGELOG README.md
%doc html
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/buku-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/buku.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_buku

%changelog
%autochangelog
