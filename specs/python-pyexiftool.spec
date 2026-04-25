Name:           python-pyexiftool
Version:        0.5.6
Release:        %autorelease
Summary:        Python wrapper for exiftool

License:        GPL-3.0-or-later OR BSD-3-Clause
URL:            https://github.com/sylikc/pyexiftool
# Sources on PyPI lack documentation
Source:         %{url}/archive/v%{version}/PyExifTool-%{version}.tar.gz
# remove error causing symbol
Patch:          doc-config-symbol-fix.patch

BuildSystem:    pyproject
BuildOption(install):  -l exiftool
BuildOption(generate_buildrequires): -x docs,test

BuildArch:      noarch
BuildRequires:  perl-Image-ExifTool
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# Docs
BuildRequires:  python3dist(installer)
BuildRequires:  graphviz
BuildRequires:  texinfo

%global _description %{expand:
PyExifTool is a Python library to communicate with an instance of Phil Harvey's
ExifTool command-line application.

The library provides the class exiftool.ExifTool that runs the command-line tool
in batch mode and features methods to send commands to that program, including
methods to extract meta-information from one or more image files. Since exiftool
is run in batch mode, only a single instance needs to be launched and can be
reused for many queries. This is much more efficient than launching a separate
process for every single query.}

%description %_description

%package -n     python3-pyexiftool
Summary:        %{summary}
Requires:       perl-Image-ExifTool

%description -n python3-pyexiftool %_description

%build -a
pushd docs
pushd source
%python3 -m installer --destdir=tempinstall %{_pyproject_wheeldir}/*.whl
PYTHONPATH="tempinstall/usr/lib/python%{python3_version}/site-packages/:$PYTHONPATH" \
 sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook pyexiftool.texi
popd
popd
popd

%install -a
mkdir -p %{buildroot}%{_datadir}/help/en/python-pyexiftool
install -m644 docs/source/texinfo/pyexiftool.xml %{buildroot}%{_datadir}/help/en/python-pyexiftool
cp -p docs/source/texinfo/*.png %{buildroot}%{_datadir}/help/en/python-pyexiftool
cp -p docs/source/texinfo/*.png.map %{buildroot}%{_datadir}/help/en/python-pyexiftool

%check -a
%pytest -v

%files -n python3-pyexiftool -f %{pyproject_files}
%doc README.rst
%doc CHANGELOG.md
%dir %{_datadir}/help/en/
%doc %lang(en) %{_datadir}/help/en/python-pyexiftool/

%changelog
%autochangelog
