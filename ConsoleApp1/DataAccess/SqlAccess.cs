﻿using ConsoleApp1.Interface.DataAccess;

namespace ConsoleApp1.DataAccess
{
    public class SqlAccess : IDataAccess
    {
        public object Value { get; private set; }

        private SqlAccess()
        {
        }

        public SqlAccess(IParam param)
        {
        }
    }
}