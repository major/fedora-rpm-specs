# Generated by go2rpm 1.9.0
# Consumes too much memory
%bcond_with check

# https://github.com/etcd-io/bbolt
%global goipath         go.etcd.io/bbolt
%global forgeurl        https://github.com/etcd-io/bbolt
Version:                1.3.7

%gometa


%global common_description %{expand:
Package Bbolt implements a low-level key/value store in pure Go. It supports
fully serializable transactions, ACID semantics, and lock-free MVCC with
multiple readers and a single writer. Bolt can be used for projects that want a
simple data store without the need to add large dependencies such as Postgres or
MySQL.

Bolt is a single-level, zero-copy, B+tree data store. This means that Bolt is
optimized for fast read access and does not require recovery in the event of a
system crash. Transactions which have not finished committing will simply be
rolled back in the event of a crash.

The design of Bolt is based on Howard Chu's LMDB database project.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        An embedded key/value database for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/bbolt

%gopkgfiles

%changelog
%autochangelog