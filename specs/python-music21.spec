Name:           python-music21
Version:        9.7.0
Release:        %autorelease
Summary:        Toolkit for computational musicology

License:        BSD-3-Clause OR LGPL-3.0-only
URL:            https://www.music21.org/music21docs/
Source0:        https://github.com/cuthbertLab/music21/releases/download/v%{version}/music21-%{version}.tar.gz

BuildRequires:  lilypond
BuildRequires:  mscore
BuildRequires:  xorg-x11-server-Xvfb

BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# Also, musescore is not built on i686.
ExcludeArch:    %{ix86}

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

# Non-standard locations that should be byte-compiled are handled below
%global _python_bytecompile_extra 0

%global _description %{expand:
Music21 is a set of tools for helping scholars and other active listeners answer
questions about music quickly and simply. It supports input of melodies in
shorthand notation, printing of musical scores, etc.}

%description %_description

%package -n python3-music21
Summary:        %{summary}
%{?python_provide:%python_provide python3-music21}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jsonpickle
BuildRequires:  python3-chardet
BuildRequires:  python3-webcolors
BuildRequires:  python3-xlrd
BuildRequires:  python3-six
BuildRequires:  python3-pillow
BuildRequires:  python3-matplotlib
BuildRequires:  python3-chardet
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-more-itertools
Requires:       python3-chardet
Requires:       python3-jsonpickle
Requires:       python3-webcolors
Requires:       python3-xlrd
Requires:       python3-six
Requires:       python3-pillow
Requires:       python3-matplotlib
# Requires:       python3-pyaudio
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       lilypond
Requires:       mscore
Requires:       %{name}-common = %{version}-%{release}

%description -n python3-music21 %_description

%package common
Summary: Music corpus and other shared files for music21
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < 6.7

%description common
%{summary}.

%prep
%autosetup -n music21-%{version} -p1

sed -i 's/numpy<2\.0\.0/numpy/' PKG-INFO pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/music21/corpus \
         %{buildroot}%{_datadir}/music21/scale/scala
mv -v %{buildroot}%{python3_sitelib}/music21/corpus/[a-z]*/ \
      %{buildroot}%{_datadir}/music21/corpus/
mv -v %{buildroot}%{python3_sitelib}/music21/scale/scala/scl \
      %{buildroot}%{_datadir}/music21/scale/scala/

ln -sv --relative %{buildroot}%{_datadir}/music21/corpus/* %{buildroot}%{python3_sitelib}/music21/corpus/
ln -sv --relative %{buildroot}%{_datadir}/music21/scale/scala/scl %{buildroot}%{python3_sitelib}/music21/scale/scala/

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/music21/

%check
mkdir -p ~/Desktop

# disable test that requires network
sed -r -i 's/testParseURL\(self\):/__disabled__\0/' music21/converter/__init__.py

PYTHONPATH=%{buildroot}%{python3_sitelib} \
LC_ALL=C.utf8 \
    xvfb-run -a \
    %{python3} -c 'import sys; from music21.test.multiprocessTest import mainPoolRunner as tm; sys.exit(tm())'

%files -n python3-music21
%{python3_sitelib}/music21/
%exclude %{python3_sitelib}/music21/LICENSE
%{python3_sitelib}/music21-%{version}.dist-info/

%files common
%license LICENSE
%doc README.md
%{_datadir}/music21/

%changelog
%autochangelog
