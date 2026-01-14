Name:           R-R.oo
Version:        %R_rpm_version 1.27.1
Release:        %autorelease
Summary:        R Object-Oriented Programming with or without References

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Methods and classes for object-oriented programming in R with or without
references.  Large effort has been made on making definition of methods as
simple as possible with a minimum of maintenance for package developers.
The package has been developed since 2001 and is now considered very
stable.  This is a cross-platform package implemented in pure R that
defines standard S3 classes without any tricks.

%prep
%autosetup -c
# Fix line endings.
for file in R.oo/inst/CITATION; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done
# Fix encoding.
file=R.oo/NEWS.md
iconv -f latin1 -t UTF-8 ${file} > ${file}.new
touch -r ${file} ${file}.new
mv ${file}.new ${file}

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
