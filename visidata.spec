%global srcname visidata

Name:           %{srcname}
Version:        3.0.2
Release:        %autorelease
Summary:        Terminal interface for exploring and arranging tabular data

License:        GPL-3.0-only
URL:            https://visidata.org
Source0:        %pypi_source %{srcname}
# Fedora specific:
Patch:          0001-Remove-extra-copy-of-man-page.patch
# Fix Desktop file validation
Patch:          https://github.com/saulpw/visidata/commit/3c4f032b72fb32c8e671b9d66f1e1edaa7181c4b.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

Requires:       python3-%{srcname} = %{version}-%{release}

%description
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%package -n     python3-%{srcname}
Summary:        %{summary}

# Optional dependencies
Recommends: python3dist(PyYAML)
Recommends: python3dist(datapackage)
Recommends: python3dist(dnslib)
Recommends: python3dist(dpkt)
Recommends: python3dist(fonttools)
Recommends: python3dist(h5py)
Recommends: python3dist(lxml)
Recommends: python3dist(mapbox-vector-tile)
Recommends: python3dist(namestand)
Recommends: python3dist(numpy)
Recommends: python3dist(openpyxl)
Recommends: python3dist(pandas) >= 0.19.2
Recommends: python3dist(pdfminer-six)
Recommends: python3dist(psycopg2)
Recommends: python3dist(pypng)
Recommends: python3dist(pyshp)
Recommends: python3dist(requests)
Recommends: python3dist(sas7bdat)
Recommends: python3dist(savReaderWriter)
Recommends: python3dist(tabulate)
Recommends: python3dist(vobject)
Recommends: python3dist(wcwidth)
Recommends: python3dist(xlrd)
Recommends: python3dist(xport)

%description -n python3-%{srcname}
VisiData is an interactive multitool for tabular data. It combines the clarity
of a spreadsheet, the efficiency of the terminal, and the power of Python, into
a lightweight utility which can handle millions of rows with ease.


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{srcname}.desktop

%check
mkdir HOME
touch HOME/.visidatarc  # Needed for TestCommands.test_baseCommands
export HOME=$PWD/HOME
%{pytest}

%files
%{_bindir}/visidata
%{_bindir}/vd2to3.vdx
%{_bindir}/vd
%{_mandir}/man1/vd.1*
%{_mandir}/man1/visidata.1*
%{_datadir}/applications/%{srcname}.desktop

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.gpl3

%changelog
%autochangelog
