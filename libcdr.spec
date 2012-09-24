%define min_ver 0.0

%define major 0
%define libname %mklibname cdr %major
%define libdev %mklibname cdr -d

Name: libcdr
Version: 0.0.8
Release: %mkrel 3
Summary: A library providing ability to interpret and import Corel Draw drawings

Group: System/Libraries
License: GPLv2+ or LGPLv2+
URL: http://www.freedesktop.org/wiki/Software/libcdr
Source: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: lcms2-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: zlib-devel

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package -n %libname
Summary:    A library providing ability to interpret and import Corel Draw drawings
Group:      System/Libraries

%description -n %libname
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package -n %libdev
Summary: Development files for %{name}
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Requires: pkgconfig

%description -n %libdev
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
Group:   Books/Howtos
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform Corel Draw drawings into other formats
Group:   Books/Howtos 

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, raw.


%prep
%setup -q

mkdir m4
autoreconf -fi

%build
%configure --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make V=1


%install
%makeinstall_std 
rm -f %{buildroot}/%{_libdir}/*.la
# these binaries do nothing currently
rm -f %{buildroot}/%{_bindir}/cmx2*


%files -n %libname
%doc AUTHORS ChangeLog COPYING.*
%{_libdir}/%{name}-%min_ver.so.%{major}*


%files -n %libdev
%{_includedir}/%{name}-%min_ver
%{_libdir}/%{name}-%min_ver.so
%{_libdir}/pkgconfig/%{name}-%min_ver.pc


%files doc
%doc COPYING.*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html


%files tools
%{_bindir}/cdr2raw
%{_bindir}/cdr2xhtml




%changelog

* Wed Jul 04 2012 dmorgan <dmorgan> 0.0.8-3.mga3
+ Revision: 267749
- Fix libs packagename

* Wed Jul 04 2012 dmorgan <dmorgan> 0.0.8-2.mga3
+ Revision: 267742
- Fix provides in the devel package

* Wed Jul 04 2012 dmorgan <dmorgan> 0.0.8-1.mga3
+ Revision: 267737
- Fix configure
- imported package libcdr


* Mon Jun 11 2012 David Tardon <dtardon@redhat.com> 0.0.8-1
- new upstream release
- adds basic initial primitive uncomplete text support

* Thu Apr 26 2012 David Tardon <dtardon@redhat.com> 0.0.7-1
- new upstream release

* Tue Apr 03 2012 David Tardon <dtardon@redhat.com> 0.0.6-1
- new upstream release

* Mon Mar 19 2012 David Tardon <dtardon@redhat.com> 0.0.5-1
- new upstream release
- fix license

* Sat Mar 10 2012 David Tardon <dtardon@redhat.com> 0.0.3-2
- remove Requires: of main package from -doc subpackage

* Thu Mar 01 2012 David Tardon <dtardon@redhat.com> 0.0.3-1
- initial import
