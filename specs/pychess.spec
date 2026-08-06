%bcond docs 1
%bcond tests 1
# extras
%bcond gbulb 1

Name:           pychess
Version:        1.1.0
Release:        %autorelease
Summary:        Chess game for GNOME

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://pychess.github.io
Source0:        https://github.com/pychess/pychess/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(sqlalchemy) >= 2
BuildRequires:  python3-gobject
BuildRequires:  gobject-introspection
BuildRequires:  gtk3
BuildRequires:  librsvg2
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sed
%if %{with docs} || %{with tests}
BuildRequires:  gstreamer1
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(websockets)
%endif
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-docs
%endif
%if %{with tests}
BuildRequires:  xwayland-run
BuildRequires:  gtksourceview4
BuildRequires:  stockfish
%endif
%if %{with gbulb}
BuildRequires:  python3dist(gbulb)
%endif

Requires:       hicolor-icon-theme
# gi.repository deps
Requires:       gobject-introspection
Requires:       gtk3
Requires:       librsvg2
Requires:       python3-gstreamer1
# for editing .pgn files
Requires:       gtksourceview4
# chess engines
Recommends:     dreamchess-engine
Recommends:     fruit
Recommends:     gnuchess
Recommends:     stockfish
Recommends:     toga2

%description
PyChess is a GTK+ chess game for Linux. It is designed to at the same time
be easy to use, beautiful to look at, and provide advanced functions for
advanced players.


%if %{with docs}
%package        doc
Summary:        Documentation for PyChess
Requires:       python3-docs

%description    doc
This package contains additional documentation for PyChess.
%endif


%if %{with gbulb}
%pyproject_extras_subpkg -n %{name} gbulb
%endif


%prep
%autosetup -n %{name}-%{version} -p1

# disable update check
cat > lib/pychess/Utils/checkversion.py <<EOF
def isgit():
    return False

async def checkversion():
    return
EOF

%if %{with docs}
# Use local intersphinx inventory
# TODO: do the same for pgi-docs once that's packaged
sed -r \
    -e 's|https://docs.python.org/3\.4|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif


%build
PYTHONPATH=${PWD}/lib %{python3} pgn2ecodb.py
PYTHONPATH=${PWD}/lib %{python3} create_theme_preview.py
%pyproject_wheel
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD}/lib sphinx-build-3 docs html
%endif


%install
%pyproject_install
%pyproject_save_files -l %{name}

desktop-file-install --delete-original               \
        --dir=%{buildroot}%{_datadir}/applications   \
        --set-key=Exec --set-value=pychess           \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet                \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%find_lang %{name}


%if %{with tests}
%check
# these tests hang
rm -f testing/{dialogs,fics*,savegame}.py
# this test requires network access
rm -f testing/remotegame.py
# run tests
PYCHESS_UNITTEST=true PYTHONPATH=lib xwfb-run -- pytest testing/*.py
%endif


%files -f %{name}.lang -f %{pyproject_files}
%doc README.md AUTHORS ARTISTS DOCUMENTERS TRANSLATORS
%doc utilities
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gtksourceview-4/language-specs/pgn.lang
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.metainfo.xml


%if %{with docs}
%files doc
%license LICENSE
%doc doc/*.dia
%doc html
%endif


%changelog
%autochangelog
