%global srcname pyocr

Name:           python-%{srcname}
Version:        0.8.5
Release:        %autorelease
Summary:        Python wrapper for OCR engines (Tesseract, Cuneiform, etc)

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/pyocr
Source:         %pypi_source %{srcname}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  tesseract
BuildRequires:  tesseract-osd
BuildRequires:  tesseract-langpack-fra
BuildRequires:  tesseract-langpack-jpn

%global _description \
A Python wrapper for Tesseract and Cuneiform

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

Recommends:     tesseract

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export LANG=C.UTF-8
%{pytest} tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md ChangeLog html

%changelog
%autochangelog
