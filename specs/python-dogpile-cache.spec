%global pypi_name dogpile_cache
%global sum A caching front-end based on the Dogpile lock
%global desc Dogpile consists of two subsystems, one building on top of the other.\
\
dogpile provides the concept of a "dogpile lock", a control structure\
which allows a single thread of execution to be selected as the\
"creator" of some resource, while allowing other threads of execution to\
refer to the previous version of this resource as the creation proceeds;\
if there is no previous version, then those threads block until the\
object is available.\
\
dogpile.cache is a caching API which provides a generic interface to\
caching backends of any variety, and additionally provides API hooks\
which integrate these cache backends with the locking mechanism of\
dogpile.\
\
Overall, dogpile.cache is intended as a replacement to the Beaker\
caching system, the internals of which are written by the same author.\
All the ideas of Beaker which "work" are re- implemented in\
dogpile.cache in a more efficient and succinct manner, and all the cruft\
(Beaker\'s internals were first written in 2005) relegated to the trash\
heap.

Name:               python-dogpile-cache
Version:            1.5.0
Release:            %autorelease
Summary:            %{sum}

License:            MIT
URL:                https://pypi.io/project/dogpile.cache
Source0:            %pypi_source

BuildArch:          noarch

%description
%{desc}


%package -n python3-dogpile-cache
Summary:  %{sum}

Requires:           python3-mako

Provides:           python3-dogpile-core = %{version}-%{release}

%description -n python3-dogpile-cache
%{desc}


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dogpile


%check
%tox


%files -n python3-dogpile-cache -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
