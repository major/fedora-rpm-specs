Name:       buku
Version:    4.9
Release:    %autorelease
Summary:    Powerful command-line bookmark manager

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/Buku
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      buku-fix-makefile.patch

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  python3-devel

%description
Buku is a powerful bookmark manager written in Python3 and SQLite3.

Buku fetches the title of a bookmarked web page and stores it along
with any additional comments and tags. You can use your favourite editor
to compose and update bookmarks. With multiple search options, including regex
and a deep scan mode (particularly for URLs), it can find any bookmark
instantly. Multiple search results can be opened in the browser at once.

%prep
%autosetup -p1
sed -i "s|urllib3>=1.23,<2|urllib3<3|" setup.py

%generate_buildrequires
%pyproject_buildrequires -x docs

%build
# generate html docs
PYTHONPATH=$PWD/build/lib sphinx-build docs/source html
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
