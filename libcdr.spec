%define api	0.1
%define major	1
%define libname %mklibname cdr %{api} %{major}
%define devname %mklibname cdr -d

Summary:	A library providing ability to interpret and import Corel Draw drawings
Name:		libcdr
Version:	0.1.7
Release:	4
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+
Url:		https://wiki.documentfoundation.org/DLP/Libraries/libcdr
Source0:	http://dev-www.libreoffice.org/src/libcdr/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(icu-uc) >= 60
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(cppunit)

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package tools
Summary:	Tools to transform Corel Draw drawings into other formats
Group:		Books/Howtos 

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, raw.

%package -n %{libname}
Summary:	A library providing ability to interpret and import Corel Draw drawings
Group:		System/Libraries

%description -n %{libname}
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure --disable-werror

sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
  -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install
# these binaries do nothing currently
rm -f %{buildroot}/%{_bindir}/cmx2*

%files tools
%{_bindir}/cdr2raw
%{_bindir}/cdr2text

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING.*
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_bindir}/cdr2xhtml

